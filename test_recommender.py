"""
Siddhant Khairnar. EE551 – Engineering Programming: Python. Fall 2025.

This module contains pytest unit tests for the TVShow and ShowRecommender
classes. These tests verify that shows can be added correctly and that
filtering and recommendation logic behaves as expected.
"""
import sys
import os
import pytest

#had to add this section to get the program to run on my computer
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.tv_show import TVShow
from src.show_recommender import ShowRecommender


@pytest.fixture
def sample_recommender():
    """
    This pytest fixture creates a ShowRecommender instance populated
    with sample TVShow objects. It is reused across multiple tests
    to avoid duplication.
    """
    recommender = ShowRecommender()

    show1 = TVShow("Breaking Bad", ["Drama", "Crime"], 62, 9.5, "en", 2008)
    show2 = TVShow("Friends", ["Comedy"], 236, 8.9, "en", 1994)
    show3 = TVShow("Dark", ["Sci-Fi", "Drama"], 26, 8.8, "de", 2017)

    recommender.add_show(show1)
    recommender.add_show(show2)
    recommender.add_show(show3)

    return recommender


def test_add_show_increases_count(sample_recommender):
    """
    Test that adding TVShow objects correctly increases the total count.
    """
    assert sample_recommender.get_total_shows() == 3


def test_filter_by_genre(sample_recommender):
    """
    Test that filtering by genre returns only shows matching that genre.
    """
    drama_shows = sample_recommender.filter_by_genre("Drama")
    assert len(drama_shows) == 2
    for show in drama_shows:
        assert "Drama" in show.genre


def test_filter_by_rating(sample_recommender):
    """
    Test that filtering by minimum rating returns only high-rated shows.
    """
    high_rated = sample_recommender.filter_by_rating(9.0)
    assert len(high_rated) == 1
    assert high_rated[0].title == "Breaking Bad"


def test_get_recommendations_limit(sample_recommender):
    """
    Test that get_recommendations respects the limit parameter.
    """
    recommendations = sample_recommender.get_recommendations(limit=2)
    assert len(recommendations) == 2


def test_search_by_title(sample_recommender):
    """
    Test that searching by title returns correct matches (case-insensitive).
    """
    results = sample_recommender.search_by_title("dark")
    assert len(results) == 1
    assert results[0].title == "Dark"


def test_statistics(sample_recommender):
    """
    Test that statistics are computed correctly for the show collection.
    """
    stats = sample_recommender.get_statistic()
    assert stats["total_shows"] == 3
    assert stats["total_episodes"] > 0
    assert stats["avg_rating"] > 0


"""Gianna Adamo. EE551- Final Project. Fall 2025. I added PyTests for testing 
the filtering by language, by episodes, and testing to get top rated shows. """

def test_filter_by_language():
    """Test filtering shows by language"""
    recommender = ShowRecommender()
    show1 = TVShow("Breaking Bad", ["Drama"], 62, 9.5, "en", 2008)
    show2 = TVShow("La Casa de Papel", ["Drama"], 41, 8.2, "es", 2017)
    recommender.add_show(show1)
    recommender.add_show(show2)
    
    english_shows = recommender.filter_by_language("en")
    assert len(english_shows) == 1
    assert english_shows[0].title == "Breaking Bad"

def test_filter_by_episodes():
    """Test filtering shows by episode range"""
    recommender = ShowRecommender()
    show1 = TVShow("Short Show", ["Comedy"], 10, 8.0, "en", 2020)
    show2 = TVShow("Medium Show", ["Drama"], 50, 8.5, "en", 2019)
    show3 = TVShow("Long Show", ["Drama"], 200, 9.0, "en", 2015)
    recommender.add_show(show1)
    recommender.add_show(show2)
    recommender.add_show(show3)
    
    medium_length = recommender.filter_by_episodes(min_episodes=40, max_episodes=100)
    assert len(medium_length) == 1
    assert medium_length[0].title == "Medium Show"

def test_get_top_rated_shows():
    """Test getting top N highest rated shows"""
    recommender = ShowRecommender()
    show1 = TVShow("Show A", ["Drama"], 50, 7.5, "en", 2020)
    show2 = TVShow("Show B", ["Comedy"], 30, 9.5, "en", 2019)
    show3 = TVShow("Show C", ["Drama"], 60, 8.5, "en", 2018)
    recommender.add_show(show1)
    recommender.add_show(show2)
    recommender.add_show(show3)
    
    top_2 = recommender.get_top_rated_shows(2)
    assert len(top_2) == 2
    assert top_2[0].title == "Show B"  # Highest rated
    assert top_2[1].title == "Show C"  # Second highest 