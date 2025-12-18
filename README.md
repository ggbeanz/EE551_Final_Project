# TV Show Decision Maker

## Course
EE551- Engineering Programming: Python

## Team Members
Gianna Adamo (gadamo@stevens.edu) <br/>
Siddhant Sunil Khairnar (skhairna@stevens.edu)

## Problem Description
Finding a new TV show to watch can be very overwhelming and challenging. With tens of thousands of available shows varying by genre, length, popularity, and user ratings, it's difficult to find TV shows that match your preferences. 

The **TV Show Decision Maker** is a Python program that helps find users new shows to watch based on their interests- such as the genre, number of episodes, and the average rating of the show. This program will analyze a large dataset with thousands of TV show options and will filter out and recommend options that match the user preferences.

## Dataset
The dataset we will be using for this project is: [Full TMDb TV Show Dataset 2024 (150K Shows)]
(https://www.kaggle.com/datasets/asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows) 

This dataset has information on:
- Show titles
- Number of episodes
- Average ratings
- Genres
- Original broadcast language
- Additional data

**Note:** This dataset was too large to upload to the GitHub so it has to be downloaded it from the provided link as a CSV. Make sure it is in the proper file path on your computer (it belongs in the data folder when you are testing the code).

## Program Structure
### Project Layout
tv-show-recommender/
├── README.md                 # This file    <br/>
├── requirements.txt          # Python dependencies  <br/>
├── data/                     # Dataset directory    <br/>
│   └── tv_shows_dataset.csv  <br/>
├── src/                      # Source code modules  <br/>
│   ├── __init__.py  <br/>
│   ├── tv_show.py           # TVShow class  <br/>
│   ├── show_recommender.py  # ShowRecommender class  <br/>
│   └── data_processor.py    # Data processing functions  <br/>
├── tests/                    # Test files  <br/>
│   ├── __init__.py  <br/>
│   └── test_recommender.py  <br/>
└── notebooks/  <br/>
    └── main.ipynb           # Main Jupyter Notebook program  <br/>

## Core Components

#### 1- **TVShow Class** ('src/tv_show.py')
This class stores information about individual TV Shows with their attributes and methods. 
**Attributes:**
- 'title' (str)- Show title
- 'genre' (list)- List of genres
- 'num_episodes' (int)- Total number of episodes
- 'avg_rating' (float)- Average rating (between 0-10)
- 'language' (str)- Original language
- 'year' (int)- Year the episode first aired

**Key Methods**
- '__str__()', '__repr__()': string representations
- '__eq__()', '__lt__()', '__gt__()', '__le__()', '__ge__()': comparison operators
- 'matches_genre()': checks if the show matches a genre
- 'is_highly_rated()': checks if the show meets the rating threshold
- 'get_info_dict()': converts to a dictionary

#### 2- **ShowRecommender Class** ('src/show_recommender.py')
This class manages the TV shows and provides filtering and recommendation functionality
**Relationship:** Uses composition with TVShow objects

**Key Methods**
- `add_show()`- Add single show with validation
- `add_shows_from_list()`- Bulk-add shows from dataset
- `filter_by_genre()`- Filter by genre using lambda
- `filter_by_rating()`- Filter by minimum rating
- `filter_by_episodes()`- Filter by range of episodes
- `filter_by_language()`- Filter by language
- `get_recommendations()`- Multi-criteria recommendation
- `get_top_rated_shows()`: Get highest-rated shows
- `search_by_title()`: Search shows by title
- `get_all_genres()`: List all available genres
- `get_statistic()`: Get collection statistics

#### 3- **Data Processing** ('src/data_processor.py')
This handles the loading, cleaning, and processing of the CSV Dataset

**Key Functions:**
- `load_data_from_csv()`- Loads the CSV with exception handling
- `clean_data()`- Handles missing values and formats data
- `extract_genres()`- Extracts the genre information
- `extract_year()`- Extracts the broadcast year from date strings
- `create_tvshow_objects()`- Converts the DataFrame rows to TVShow objects
- `load_and_process_data()`- Function that loads and processes the data

#### 4- **Main Program** ('notebooks/main.ipynb')
This is a Jupyter notebook file that serves as the user interface.
**Features:**
- Loads the dataset from the CSV
- Asks users for TV Show preferences (genre, episodes, language, rating)
- Displays the personalized recommendations
- Visualizes data using Matplotlib
- Shows the statistics about the collection


## Installation and Setup

### Prerequisites
Follow the requirements.txt file to make sure you have all of the necessities

## How to Use the Program
- Step 1- make sure all files are downloaded in the proper path structure
- Step 2- on the main.ipynb file in Jupyter Notebook make sure to change what is explicitly stated (ex- filepath)
- Step 3- the main.ipynb file should run and provide a working TV Show Decider



**"I pledge my honor that I have abided by the Stevens Honor System."**
