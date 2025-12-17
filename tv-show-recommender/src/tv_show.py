"""Gianna Adamo. EE551- Engineering Programming: Python. Fall 2025. TVShow Class
Module defines the TVShow class. This represents a single TV show with attributes
including the title, genre, rating, and number of episodes.
"""


class TVShow:
    """This class represents a TV show with its attributes. These attributes include
    the title of the show (which is a string), the genre or genres of the show (which
    is a string or a list), the number of episodes (which is an int), the average user
    rating from 0-10 (which is a float), the language of the show (which can be a
    string), and the year the show first aired (which can be an int).
    """

    def __init__(self, title, genre, num_episodes, avg_rating, language="en", year=None):
        """This makes the TVShow object. This includes the show title (title), genre or
        genres (genre), the number of episodes (num_episodes), the average user rating
        (avg_rating), the language of the show which defaults to English (language), and
        the year the show came out which defaults to None. This raises a ValueError if
        the rating is not between 0 and 10. A Valueerror is also raised if the number of
        episodes is a negative number.
        """

        # validate inputs
        if not 0 <= avg_rating <= 10:
            raise ValueError("Rating must be between 0 and 10.")
        if num_episodes < 0:
            raise ValueError("Number of episodes canno be a negative number.")

        self.title = title
        self.genre = genre if isinstance(genre, list) else [genre]
        self.num_episodes = num_episodes
        self.avg_rating = avg_rating
        self.language = language
        self.year = year

    def __str__(self):
        """This function returns a user-friendly string representation of the TV show."""

        genre_str = ", ".join(self.genre)
        year_str = f" ({self.year})" if self.year else ""
        return (
            f"{self.title}{year_str}\n"
            f"  Genre: {genre_str}\n"
            f"  Episodes: {self.num_episodes}\n"
            f"  Rating: {self.avg_rating}/10\n"
            f"  Language: {self.language}"
        )

    def __repr__(self):
        """This returns a string representation for debugging."""

        return (
            f"TVShow(title='{self.title}', genre={self.genre}, "
            f"num_episodes={self.num_episodes}, avg_rating={self.avg_rating}, "
            f"language='{self.language}', year={self.year})"
        )

    def __eq__(self, other):
        """This checks is 2 shows are equal, meaning they have the same title and year.
        This returns a boolean value- true if shows are equal and false elsewise.
        """

        if not isinstance(other, TVShow):
            return False
        return self.title == other.title and self.year == other.year

    def __lt__(self, other):
        """This compares TV Shows based on their rating for sorting. This returns a boolean value-
        true if the show has a lower rating than others.
        """

        if not isinstance(other, TVShow):
            return NotImplemented
        return self.avg_rating < other.avg_rating

    def __gt__(self, other):
        """This compares TV shows based on rating for comparison. This returns true if the show
        has a hgiher rating than others, false elsewise.
        """

        if not isinstance(other, TVShow):
            return NotImplemented
        return self.avg_rating > other.avg_rating

    def __le__(self, other):
        """This compares the TV shows based on their rating if they are less than or equal to
        another show. This returns true if the show has a lower or equal rating to another show.
        """

        if not isinstance(other, TVShow):
            return NotImplemented
        return self.avg_rating <= other.avg_rating

    def __ge__(self, other):
        """This compares TV shows based on their rating if they are greater than or equal to
        another show. This returns true is the show does have a higher or equal value than
        another show, and it returns false elsewise.
        """

        if not isinstance(other, TVShow):
            return NotImplemented
        return self.avg_rating >= other.avg_rating

    def matches_genre(self, target_genre):
        """This checks to see if the show matches a specific genre. This returns a
        booleran value- true if the show hs a targe genre, and false elsewise.
        """

        # case-insensitive for genres
        return any(target_genre.lower() in g.lower() for g in self.genre)

    def is_highly_rated(self, threshold=7.0):
        """This checks if the TV show is highly rated. If the show is a 7.0 or higher,
        it is highly rated and will return True, if not it will return false.
        """

        return self.avg_rating >= threshold

    def get_info_dict(self):
        """This returns the show information as a dictionary."""
        return {
            "title": self.title,
            "genre": self.genre,
            "num_episodes": self.num_episodes,
            "avg_rating": self.avg_rating,
            "language": self.language,
            "year": self.year,
        }
