"""Gianna Adamo. EE551- Engineering Programming: Python. Fall 2025. The TVShow Class 
Module defines the TVShow class. This represents a single TV show with attributes 
including the title, genre, rating, and number of episodes."""

class TVShow:
    """This class represents a TV show with its attributes. These attributes include 
    the title of the show (which is a string), the genre or genres of the show (which 
    is a string or a list), the number of episodes (which is an int), the average user 
    rating from 0-10 (which is a float), the language of the show (which can be a 
    string), and the year the show first aired (which can be an int). """


    def __init__(self, title, genre, num_episodes, avg_rating, language="en", year=None):
        """This makes the TVShow object. This includes the show title (title), genre or 
        genres (genre), the number of episodes (num_episodes), the average user rating 
        (avg_rating), the language of the show which defaults to English (language), and 
        the year the show came out which defaults to None. This raises a ValueError if 
        the rating is not between 0 and 10. A ValueError is also raised if the number of 
        episodes is a negative number."""

        #validate inputs and check if the ratings are within 0-10
        if not 0 <= avg_rating <= 10:
            raise ValueError("Rating must be between 0 and 10.")
        if num_episodes < 0:
            raise ValueError("Number of episodes cannot be a negative number.")
        
        #set instance attributes
        #store the title
        self.title = title
        #convert the genre to a list or keeps it as a list if the user inputs a list
        self.genre = genre if isinstance(genre, list) else [genre]
        #store the number of episodes
        self.num_episodes = num_episodes
        #store the average ratings
        self.avg_rating = avg_rating
        #store the language- defaults to english if not specified
        self.language = language
        #store the year- if unknown it can be None
        self.year = year

    def __str__(self):
        """This function returns a user-friendly string representation of the TV show. It uses 
        __str__. This returns a formatted string with details about the show."""

        #join multiple genres together with commas
        genre_str = ", ".join(self.genre)
        #add the year in the parentheses if available, if not, have an empty string
        year_str = f" ({self.year})" if self.year else ""
        #build a multiline string with info on the show
        return (f"{self.title}{year_str}\n"
            f"  Genre: {genre_str}\n"
            f"  Episodes: {self.num_episodes}\n"
            f"  Rating: {self.avg_rating}/10\n"
            f"  Language: {self.language}")
    
    def __repr__(self):
        """This returns a string representation for debugging. This returns a representation 
        that shows all of the attributes."""
        #this returns a string- lets you see the state of the object
        return (f"TVShow(title='{self.title}', genre={self.genre}, "
                f"num_episodes={self.num_episodes}, avg_rating={self.avg_rating}, "
                f"language='{self.language}', year={self.year})")
    
    def __eq__(self, other):
        """This checks if 2 shows are equal, meaning they have the same title and year. 
        This returns a boolean value- true if shows are equal and false elsewise."""
        #check if we are comparing with another TVShow object- if not they're not equal
        if not isinstance(other, TVShow):
            return False
        #2 shows are equal if both titles and years match- this takes care of potential reboots or remakes
        return self.title == other.title and self.year == other.year
    
    def __lt__(self, other):
        """This compares TV Shows based on their rating for sorting. This returns a boolean value- 
        true if the show has a lower rating than others."""
        #validate that we're comparing with another show
        if not isinstance(other, TVShow):
            return NotImplemented
        #compare based on avg rating- lower is less than
        return self.avg_rating < other.avg_rating
    
    def __gt__(self, other):
        """This compares TV shows based on rating for comparison. This returns true if the show 
        has a higher rating than others, false elsewise."""
        #validate that we're comparing with another show
        if not isinstance(other, TVShow):
            return NotImplemented
        #compare based on avg rating- higher is greater than
        return self.avg_rating > other.avg_rating
    
    def __le__(self, other):
        """This compares the TV shows based on their rating if they are less than or equal to 
        another show. This returns true if the show has a lower or equal rating to another show."""
        #validate we're comparing with another show
        if not isinstance(other, TVShow):
            return NotImplemented
        #compare based on the average rating- less than or equal to
        return self.avg_rating <= other.avg_rating
    
    def __ge__(self, other):
        """This compares TV shows based on their rating if they are greater than or equal to 
        another show. This returns true if the show does have a higher or equal value than 
        another show, and it returns false elsewise."""
        #validate that we're comparing with another show
        if not isinstance(other, TVShow):
            return NotImplemented
        #compare based on the average rating- greater than or equal to
        return self.avg_rating >= other.avg_rating
    
    def matches_genre(self, target_genre):
        """This checks to see if the show matches a specific genre. This returns a 
        boolean value- true if the show has a target genre, and false elsewise."""

        #case-insensitive for genres
        #any() returns True if at least one genre matches, 'in' operator allows partial matches 
        return any(target_genre.lower() in g.lower() for g in self.genre)
    
    def is_highly_rated(self, threshold = 7.0):
        """This checks if the TV show is highly rated. If the show is a 7.0 or higher, 
        it is highly rated and will return True, if not it will return false."""
        
        return self.avg_rating >= threshold
    
    def get_info_dict(self):
        """This returns the show information as a dictionary."""
        #this makes and returns a dictionary with all the show info
        return {
            'title': self.title,
            'genre': self.genre,
            'num_episodes': self.num_episodes,
            'avg_rating': self.avg_rating,
            'language': self.language,
            'year': self.year
        }

'''
#example code I used to test. To run this remove the docstring quotes and run the file
if __name__ == "__main__":
    #make sample TV shows
    show1 = TVShow("Breaking Bad", ["Drama", "Crime"], 62, 9.5, "en", 2008)
    show2 = TVShow("Stranger Things", "Sci-Fi", 42, 8.7, "en", 2016)
    show3 = TVShow("The Office", "Comedy", 201, 9.0, "en", 2005)
    
    #test __str__ 
    print("Show 1 Details:")
    print(show1)
    print()
    
    #test __repr__ 
    print("Show 2 Repr:")
    print(repr(show2))
    print()
    
    #test comparison operators
    print(f"Is Breaking Bad higher rated than The Office? {show1 > show3}")
    print()
    
    #test genre matching
    print(f"Does Stranger Things match Sci-Fi? {show2.matches_genre('Sci-Fi')}")
    print(f"Does The Office match Drama? {show3.matches_genre('Drama')}")
    print()
    
    #test highly rated check
    print(f"Is Breaking Bad highly rated (>7)? {show1.is_highly_rated()}")
    print()
    
    #test get_info_dict
    print("Show 3 as dictionary:")
    print(show3.get_info_dict())
'''