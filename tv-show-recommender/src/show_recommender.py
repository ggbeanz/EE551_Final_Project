from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Sequence

from .tv_show import TVShow


@dataclass(slots=True)
class ShowRecommender:
    shows: List[TVShow] = field(default_factory=list)

    def add_show(self, show: TVShow) -> None:
        self.shows.append(show)

    def get_total_shows(self) -> int:
        return len(self.shows)

    def filter_by_genre(self, genre: str) -> List[TVShow]:
        genre_key = (genre or "").strip().lower()
        if not genre_key:
            return []

        return [
            show
            for show in self.shows
            if any(g.strip().lower() == genre_key for g in show.genre)
        ]

    def filter_by_rating(self, min_rating: float) -> List[TVShow]:
        return [show for show in self.shows if show.avg_rating >= float(min_rating)]

    def get_recommendations(self, limit: int = 5) -> List[TVShow]:
        ranked: Sequence[TVShow] = sorted(
            self.shows, key=lambda show: (-show.avg_rating, show.title.lower())
        )
        if limit is None:
            return list(ranked)
        return list(ranked[: max(0, int(limit))])

    def search_by_title(self, query: str) -> List[TVShow]:
        q = (query or "").strip().lower()
        if not q:
            return []
        return [show for show in self.shows if q in show.title.lower()]

    def get_statistic(self) -> dict:
        total_shows = len(self.shows)
        total_episodes = sum(show.num_episodes for show in self.shows)
        avg_rating = (
            sum(show.avg_rating for show in self.shows) / total_shows
            if total_shows
            else 0.0
        )

        return {
            "total_shows": total_shows,
            "total_episodes": total_episodes,
            "avg_rating": avg_rating,
        }
