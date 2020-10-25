from datetime import date
from movies.domain.modelMain import Movie, Genre, Director, Actor, Review, make_review, User
import pytest

@pytest.fixture()
def movie():
    return Movie(
        "Guardians of the Galaxy",
        2014
    )

@pytest.fixture()
def user():
    return User('dbowie', '1234567890')

@pytest.fixture()
def actor():
    return Actor('John Krasinski')

@pytest.fixture()
def genre():
    return Genre('Drama')

@pytest.fixture()
def director():
    return Director('Michael Bay')

def test_user_construction(user):
    assert user.username == 'bmackle'
    assert user.password == '2637163826'
    assert repr(user) == '<User bmackle 2637163826>'

    for review in user.reviews:
        assert False

def test_movie_construction(movie):
    assert movie.id is None
    assert movie.year == 2014
    assert movie.title == 'Guardians of the Galaxy'

    assert len(movie.reviews) == 0
    assert len(movie.actors) == 0
    assert len(movie.genres) == 0
    assert movie.director is None
    assert repr(movie) == '<Movie Guardians of the Galaxy, 2014>'

def test_article_less_than_operator(movie):
    movie1 = Movie(
        "Apples",
        None
    )

    movie2 = Movie(
        'Guardians of the Galaxy',
        2020
    )

    assert movie1 < movie
    assert movie < movie2

def test_actor_construction(actor):
    assert actor.actor_full_name == 'Tina Fey'
    for colleague in actor.colleagues:
        assert False

def test_make_review_establishes_relationships(movie, user):
    review_text = 'very bad'
    review = make_review(review_text=review_text, user=user, movie=movie)

    assert review in user.reviews
    assert review.user is user
    assert review in movie.reviews
    assert review.movie is movie

