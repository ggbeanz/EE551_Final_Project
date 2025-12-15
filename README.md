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

#### 1- **TVShow Class**
This class stores information about individual TV Shows. It includes the attributes: title, genre, episodes, rating, and language. This is the method 
