"""
Siddhant Khairnar. EE551 – Engineering Programming: Python. Fall 2025.

This module contains pytest unit tests for the TVShow and ShowRecommender
classes. These tests verify that shows can be added correctly and that
filtering and recommendation logic behaves as expected.
"""
import sys
import os
import pytest


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
