from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

##POST METHODS##

#User Register
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect ('/')
    new_user= {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id=User.save(new_user)
    session['user_id'] = id
    flash("You're now logged in")
    return redirect('/recipes')

#User Login
@app.route('/login', methods=['POST'])
def login():
    data={
        'email': request.form['email']
    }
    user=User.get_user_email(data)
    if not user:
        flash("That email is not in our database, please register")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong password")
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("You're now logged in")
        return redirect('/recipes')

