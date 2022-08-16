from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User

bcrypt=Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return redirect ('/dashboard')

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
    print("new_user", new_user)
    id=User.save(new_user)
    print("id", id)
    # if not id:
    #     flash("Something went wrong")
    #     return redirect('/')
    session['user_id'] = id
    flash("You're now logged in")
    print("session", id)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data={
        'email': request.form['email']
    }
    user=User.user_email(data)
    if not user:
        flash("That email is not in our database, please register")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong password")
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("You're now logged in")
        return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data={
            'id': session['user_id']
        }
        theUser=User.get_user_id(data)
        return render_template("dashboard.html", user=theUser)
