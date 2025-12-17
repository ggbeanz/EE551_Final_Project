import argparse

from src.data_processor import load_tv_shows_from_tmdb_csv
from src.show_recommender import ShowRecommender


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Preview-loading the Kaggle TMDB TV dataset into the recommender."
    )
    parser.add_argument("--csv", required=True, help="Path to TMDB_tv_dataset_v3.csv")
    parser.add_argument(
        "--limit",
        type=int,
        default=1000,
        help="Max rows to load (use 0 to load none).",
    )
    parser.add_argument(
        "--show",
        type=int,
        default=10,
        help="How many loaded shows to print.",
    )
    args = parser.parse_args()

    tv_shows = load_tv_shows_from_tmdb_csv(args.csv, limit=args.limit)
    recommender = ShowRecommender()
    recommender.add_shows_from_list(tv_shows)

    print(f"Loaded {recommender.get_total_shows()} shows from: {args.csv}")
    stats = recommender.get_statistic()
    print(f"Stats: {stats}")
    print()

    for index, show in enumerate(tv_shows[: max(0, args.show)], 1):
        print(f"{index}. {show.title} ({show.avg_rating}/10) [{', '.join(show.genre)}]")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

