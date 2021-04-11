"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(score, movie, user):
    """Create and return a new rating."""

    rating = Rating(score=score, movie=movie, user=user)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movies():
    """Returns movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """"Return all movies by ID."""

    return Movie.query.get(movie_id)

def get_users():
    """Returns users."""

    return User.query.all()

def get_user_by_id(user_id):
    """"Return all users by ID."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return user if exists."""

    return User.query.filter(User.email == email).first()

def is_correct_password(email, password):
    """Checks if password is correct"""

    user = get_user_by_email(email)
    
    if user != None: 
        return user.password == password

if __name__ == '__main__':
    from server import app
    connect_to_db(app)