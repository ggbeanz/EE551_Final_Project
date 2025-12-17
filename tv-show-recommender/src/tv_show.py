from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True, slots=True)
class TVShow:
    title: str
    genre: List[str]
    num_episodes: int
    avg_rating: float
    language: str
    year: int

    def __post_init__(self) -> None:
        normalized_title = (self.title or "").strip()
        normalized_language = (self.language or "").strip()

        genre_value = self.genre
        if isinstance(genre_value, str):
            genre_list = [g.strip() for g in genre_value.split(",") if g.strip()]
        elif isinstance(genre_value, Iterable):
            genre_list = [str(g).strip() for g in genre_value if str(g).strip()]
        else:
            genre_list = []

        object.__setattr__(self, "title", normalized_title)
        object.__setattr__(self, "language", normalized_language)
        object.__setattr__(self, "genre", genre_list)
