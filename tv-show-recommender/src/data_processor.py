"""
Siddhant Khairnar. EE551 – Engineering Programming: Python. Fall 2025.
The data_processor module is responsible for loading, cleaning,
and preparing TV show data from a CSV file. It converts raw dataset
rows into TVShow objects that can be used by the ShowRecommender class.
"""

import csv
from typing import List

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

    # list that will store all valid TVShow objects
    tv_shows = []

    try:
        # open the CSV file safely
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            # loop through each row in the dataset
            for row in reader:
                try:
                    # extract and clean string fields
                    title = row.get("title", "").strip()
                    language = row.get("language", "").strip()

                    # genre can be stored as a string or list-like format
                    genre = row.get("genre", "")
                    if isinstance(genre, str):
                        # split genres if they are comma-separated
                        genre = [g.strip() for g in genre.split(",") if g.strip()]

                    # convert numeric values safely
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
                    # skip rows with invalid numeric data
                    continue

    except FileNotFoundError:
        # raise a clear error if dataset is missing
        raise FileNotFoundError(f"CSV file not found at: {file_path}")

    # return the fully processed list of TVShow objects
    return tv_shows
