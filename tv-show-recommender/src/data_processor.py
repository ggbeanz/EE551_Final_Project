"""
Siddhant Khairnar. EE551 – Engineering Programming: Python. Fall 2025.
The data_processor module is responsible for loading, cleaning,
and preparing TV show data from a CSV file. It converts raw dataset
rows into TVShow objects that can be used by the ShowRecommender class.
"""

# This module supports two CSV formats:
# 1) A simple/cleaned project CSV with columns like title/genre/episodes/rating/year.
# 2) The Kaggle TMDB TV dataset (v3) with columns like name/genres/number_of_episodes/vote_average.
#
# Both loaders are defensive: they skip rows with missing/invalid numeric data so the program
# continues to run even if the dataset has inconsistencies.

import csv
from typing import List, Optional

from .tv_show import TVShow


def load_tv_shows_from_csv(file_path: str) -> List[TVShow]:
    """
    This function loads TV show data from a CSV file and converts each
    valid row into a TVShow object.

    The function also performs basic validation and error handling to
    ensure that incorrect or missing data does not crash the program.

    Args:
        file_path (str): Path to the CSV dataset file.

    Returns:
        List[TVShow]: A list of TVShow objects created from the dataset.
    """

    # List that will store all valid TVShow objects.
    tv_shows = []

    try:
        # Open the CSV file safely.
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            # Loop through each row in the dataset.
            for row in reader:
                try:
                    # Extract and clean string fields.
                    title = row.get("title", "").strip()
                    language = row.get("language", "").strip()

                    # Genre can be stored as a string or list-like format.
                    genre = row.get("genre", "")
                    if isinstance(genre, str):
                        # split genres if they are comma-separated
                        genre = [g.strip() for g in genre.split(",") if g.strip()]

                    # Convert numeric values safely.
                    num_episodes = int(row.get("episodes", 0))
                    avg_rating = float(row.get("rating", 0))
                    year = int(row.get("year", 0))

                    # create a TVShow object
                    show = TVShow(
                        title=title,
                        genre=genre,
                        num_episodes=num_episodes,
                        avg_rating=avg_rating,
                        language=language,
                        year=year
                    )

                    # add valid show to the list
                    tv_shows.append(show)

                except (ValueError, TypeError):
                    # Skip rows with invalid numeric data.
                    continue

    except FileNotFoundError:
        # Raise a clear error if dataset is missing.
        raise FileNotFoundError(f"CSV file not found at: {file_path}")

    # return the fully processed list of TVShow objects
    return tv_shows


def load_tv_shows_from_tmdb_csv(file_path: str, limit: Optional[int] = 1000) -> List[TVShow]:
    """
    Load TV show data from the Kaggle TMDB TV dataset (v3) CSV file and convert each
    valid row into a TVShow object.

    Expected TMDB columns:
        - name -> title
        - genres -> genre (comma-separated string)
        - number_of_episodes -> num_episodes
        - vote_average -> avg_rating
        - original_language -> language
        - first_air_date -> year (YYYY extracted from YYYY-MM-DD)

    Args:
        file_path (str): Path to the TMDB CSV dataset file.
        limit (Optional[int]): Max number of valid rows to load. Use None for no limit.

    Returns:
        List[TVShow]: List of TVShow objects loaded from the dataset.
    """
    tv_shows: List[TVShow] = []
    max_valid = None if limit is None else max(0, int(limit))

    try:
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                # Stop once we have loaded the requested number of valid rows.
                if max_valid is not None and len(tv_shows) >= max_valid:
                    break

                try:
                    # Map TMDB column names into our TVShow fields.
                    title = (row.get("name") or "").strip()
                    language = (row.get("original_language") or "").strip()

                    # TMDB stores genres as a comma-separated string; split into a list.
                    genres_raw = (row.get("genres") or "").strip()
                    genre = [g.strip() for g in genres_raw.split(",") if g.strip()]

                    # Convert numeric values required by TVShow.
                    num_episodes = int(row.get("number_of_episodes") or 0)
                    avg_rating = float(row.get("vote_average") or 0)

                    # Convert first air date (YYYY-MM-DD) into a year integer.
                    first_air_date = (row.get("first_air_date") or "").strip()
                    year = int(first_air_date[:4]) if len(first_air_date) >= 4 else None

                    show = TVShow(
                        title=title,
                        genre=genre,
                        num_episodes=num_episodes,
                        avg_rating=avg_rating,
                        language=language,
                        year=year,
                    )

                    tv_shows.append(show)

                except (ValueError, TypeError):
                    # Skip any invalid row (bad numbers or missing data).
                    continue

    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at: {file_path}")

    return tv_shows
