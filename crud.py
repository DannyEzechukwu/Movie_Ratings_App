"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_users():
    return User.query.all()

def get_user_by_id(user_id):
    
    return User.query.get(user_id)

def get_user_by_email(email): 
    # users = User.query.all()
    # for user in users: 
    #     if user.email == email: 
    #         return user.email
    
    # return None

    return User.query.filter(User.email == email).first()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    # movie = Movie(movie_title = title, movie_overview = overview, movie_release_date = release_date, poster_path = poster_path)
    movie = Movie(title, overview, release_date, poster_path)

    return movie

def create_rating(score , movie_id, user_id):
    """Create and return a new user."""

    rating = Rating(score = score, r_movie_id =  movie_id, r_user_id = user_id)

    return rating

def get_movies(): 
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)