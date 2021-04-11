"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ View homepage"""
    return render_template('homepage.html')


@app.route('/movies')
def all_movies(): 
    """"View movies."""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """View movie details."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_users():
    """View users."""

    users = crud.get_users()

    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def show_user_details(user_id):
    """View user details."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user.""" 

    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)

    if user:
        flash('That account is already taken. Use a different email to create an account.')
    else:
        crud.create_user(email, password)
        flash('You have successfully created an account. You can now log in.')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user."""
    
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)
    correct_password = crud.is_correct_password(email, password)

    if correct_password: 
        session['user'] = user.user_id
        flash('You have been logged in!')
    else: 
        flash('Uh oh! Try again.')

    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
