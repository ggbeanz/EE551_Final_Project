"""Gianna Adamo. EE551- Engineering Programming: Python. Fall 2025. The ShowRecommender Class module
defines that ShowRecommender class. This manages TV shows and provides filtering and recommendations
based on the user preferences.
"""

from .tv_show import TVShow


class ShowRecommender:
    """This class manages the collection of TV shows and provides recommendations. It uses composition
    since it has multiple TVShow objects and it provides methods to filter and recommend shows based
    on the user standards. For the final project this class will hold all of the shows from the fataset
    and it will let users find their next show to watch.
    """

    def __init__(self):
        """This starts the ShowRecommender with an empty list of TV Shows."""
        # list that stores the TVShow objects
        # when the project is done- this will have all of the shows from the dataset
        self.shows = []

    def add_show(self, show):
        """This adds a TV show object to the collection. A TypeError is raised if the provided
        object isn't a TVShow instance.
        """
        # validate that we are only adding TVShow objects
        if not isinstance(show, TVShow):
            raise TypeError("Only TVShow objects can be added.")
        # add validated show to the collection
        self.shows.append(show)

    def add_shows_from_list(self, show_list):
        """This adds multiple TV Shows from the list. This is useful when loading many shows from the
        dataset. add_show() is used to make sure each show is validated.
        """
        # this loops through each show and adds it- this validates each show
        for show in show_list:
            self.add_show(show)

    def get_total_shows(self):
        """This returns the total number of shows that are in the collection. This is good for
        showing statistics to the ser about how many shows are available in the dataset. This returns
        an int.
        """
        return len(self.shows)

    def filter_by_genre(self, genre):
        """This filters the shows by a specific genre by using filter() with a lambda expression. It
        returns a list of TVShow objects that match the genre.
        """
        # use filters and lambda to find matching shows
        # lambda function calls each shows' matches_genre()
        return list(filter(lambda show: show.matches_genre(genre), self.shows))

    def filter_by_rating(self, min_rating):
        """This uses list comprehension to filter shows and it only returns shows with ratings
        that are the same or above the minimum threshold.
        """
        # uses list comprehension to filter the shows
        # checks each shows' avg_rating against the min
        return [show for show in self.shows if show.avg_rating >= min_rating]

    def filter_by_episodes(self, min_episodes=None, max_episodes=None):
        """This filters TV shows by their number of episodes by minimum, maximum, or both. This is
        useful when users what to find a shorter show or a longer show depending on their preferences.
        This returns a list of TV show objects that are within the episode range.
        """
        # start with all shows
        filtered_shows = self.shows
        # apply the minimum episode filter if prompted
        if min_episodes is not None:
            # list comprehension to keep only shows with enough episodes
            filtered_shows = [show for show in filtered_shows if show.num_episodes >= min_episodes]
        # apply maximum episode filter if prompted
        if max_episodes is not None:
            # list comprehension to keep only shows within the limit of episodes
            filtered_shows = [show for show in filtered_shows if show.num_episodes <= max_episodes]

        return filtered_shows

    def filter_by_language(self, language):
        """This filters the shows by language. This returns the list of TVShow objects in the specific
        language.
        """
        # uses list comprehension with that is case-insensitive
        return [show for show in self.shows if show.language.lower() == language.lower()]

    def get_recommendations(
        self,
        genre=None,
        min_rating=None,
        min_episodes=None,
        max_episodes=None,
        language=None,
        limit=10,
    ):
        """This gets show recommendations based on multiple criteria. It returns a list of recommended
        TVShow objects that are sorted by the rating. This is the main aspect of recommending shows.
        This method will be the main part in returning recommendations to the user in the main file.
        """

        # start with all show options
        recommendations = self.shows

        # apply genre filter if the user specified this
        if genre:
            # keep only shows that match the specified genre
            recommendations = [show for show in recommendations if show.matches_genre(genre)]

        # apply min rating filter if the user specified
        if min_rating is not None:
            # keep only shows that are rated at or above the minimum criteria
            recommendations = [show for show in recommendations if show.avg_rating >= min_rating]
        # apply min episode filter if specified
        if min_episodes is not None:
            # keep only the shows that have enough episodes
            recommendations = [show for show in recommendations if show.num_episodes >= min_episodes]
        # apply max episode filter if specified
        if max_episodes is not None:
            # keep only shows that are within the episode limits
            recommendations = [show for show in recommendations if show.num_episodes <= max_episodes]
        # apply language filter if specified
        if language:
            # keep shows only in specified language
            recommendations = [
                show for show in recommendations if show.language.lower() == language.lower()
            ]

        # sort the ratings from highest to lowest and return a limited number of results
        # uses __lt__ from TVShow Class
        recommendations.sort(reverse=True)
        # returns the top limit number of recommendations
        return recommendations[:limit]

    def get_top_rated_shows(self, n=10):
        """This gets the top N highest rated shows. The number of shows to return defaults to 10. This will return a list of the top N highest
        rated TVShow objects.
        """
        # short shows by highest rating first using the TVShow's comparison operator
        sorted_shows = sorted(self.shows, reverse=True)
        # return only top N shows
        return sorted_shows[:n]

    def get_all_genres(self):
        """This gets a list of all the genres. It returns a sorted list of genre strings. This helps show users what genre options are
        available.
        """
        # this uses a set to handle duplicates
        all_genres = set()
        # this loops through each show in the collection
        for show in self.shows:
            # each show can have multiple genres so loop through and check them
            for genre in show.genre:
                # add each genre to our set, ignoring duplicates
                all_genres.add(genre)
        # convert the set to a sorted list
        return sorted(list(all_genres))

    def get_shows_by_year(self, year):
        """This gets all of the shows that aired in a specific year. The specific year is an int. This returns a list of TVShow objects from
        that year.
        """
        # uses list comprehension to find all shows from the selected year
        return [show for show in self.shows if show.year == year]

    def search_by_title(self, search_term):
        """This looks for shows based on their title. This is case-insensitive. search_term searches in titles. This returns a list of
        TVShow objects with the same titles.
        """
        # convert the search to lowercase for case-insensitive matching
        search_term = search_term.lower()
        # uses list comprehension to find shows with matching titles; uses 'in' for shows that partially match
        return [show for show in self.shows if search_term in show.title.lower()]

    def get_statistic(self):
        """This gets the statistics about the show collection. This returns a dictionary with the statistics."""
        # handles edge case of empty collection
        if not self.shows:
            # returns 0s for empty collections
            return {"total_shows": 0, "avg_rating": 0, "total_episodes": 0, "total_genres": 0}
        # find total episodes across all shows using sum() and generator
        total_episodes = sum(show.num_episodes for show in self.shows)
        # find avg rating across all shows
        avg_rating = sum(show.avg_rating for show in self.shows) / len(self.shows)
        # return a dict with all of the statistics
        return {
            "total_shows": len(self.shows),
            "avg_rating": round(avg_rating, 2),
            "total_episodes": total_episodes,
            "total_genres": len(self.get_all_genres()),
        }

    def __str__(self):
        # This returns a string representation of the recommender
        return f"ShowRecommender with {len(self.shows)} shows"

    def __repr__(self):
        # This returns a technical string representation thats good for debugging
        return f"ShowRecommender(shows = {len(self.shows)})"
