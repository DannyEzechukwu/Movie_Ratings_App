"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect

from model import connect_to_db, db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def get_all_movies():
    if 'id' in session:
        movies = crud.get_movies()
        return render_template('movies.html', movies = movies)
    
    return redirect('/')

@app.route('/movies/<movie_id>')
def get_movie(movie_id):
    if 'id' in session: 

        movie = crud.get_movie_by_id(movie_id)

        return render_template("movie_details.html", movie=movie)

    return redirect('/')
    

@app.route('/users')
def get_users():
    if 'id' in session:

        users = crud.get_users()
        return render_template("users.html", users = users)

    return redirect('/')

@app.route('/users/<user_id>')
def get_user(user_id):
    if 'id' in session:
        user = crud.get_user_by_id(user_id)
        return render_template("user_details.html", user = user)

    return redirect('/')


@app.route('/new_users', methods = ['POST'])
def register_user(): 
    input_email = request.form.get('email')
    input_password = request.form.get('password')

    if crud.get_user_by_email(input_email): 
        flash('You cannot create an account with this email. Try again.')
        return redirect('/')
    else: 
        new_user = crud.create_user(email = input_email, password =input_password)
        session['id'] = new_user.user_id
        db.session.add(new_user)
        db.session.commit()

        flash('New user added!')
        return redirect("/movies")
    
    
@app.route('/login', methods = ['POST'])
def login(): 
    input_email = request.form.get('email')
    input_password = request.form.get('password')

    users = crud.get_users() 

    for user in users: 
        if user.email == input_email and  user.password == input_password:
            session['id'] = user.user_id
            flash('Logged in!')
            return redirect('/movies')
    
    flash('Username or email incorrect!')
    return redirect('/')

@app.route('/new_rating/<movie_id>', methods = ['POST'])
def add_rating(movie_id): 
    score = request.form.get('rating')
    
    if 'id' in session: 
        rating = crud.create_rating(int(score), 
                                    movie_id, 
                                    session['id'])
        db.session.add(rating)
        db.session.commit()
        flash('Rating added!')

    return redirect('/')


    
    
    


    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
