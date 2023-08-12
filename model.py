"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=False):
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        flask_app.config["SQLALCHEMY_ECHO"] = echo
        flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        db.app = flask_app
        db.init_app(flask_app)

        print("Connected to the db!")


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    rating = db.relationship("Rating", back_populates = "user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):
    __tablename__ = "movie"

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    movie_title = db.Column(db.String)
    movie_overview = db.Column(db.Text)
    movie_release_date= db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    rating = db.relationship("Rating", back_populates = "movie")

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.movie_title}>'

class Rating(db.Model):
    __tablename__ = "rating"

    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    score = db.Column(db.Integer)
    r_movie_id = db.Column(db.Integer,db.ForeignKey("movie.movie_id"))
    r_user_id =  db.Column(db.Integer,db.ForeignKey("user.user_id"))

    movie = db.relationship("Movie", back_populates = "rating")
    user = db.relationship("User", back_populates = "rating")
   
    def __repr__(self):
         return f'<Rating rating_id={self.rating_id} score={self.score}>'

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)
