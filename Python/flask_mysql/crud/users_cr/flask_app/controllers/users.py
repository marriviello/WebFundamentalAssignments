from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users/')

@app.route('/create/',methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect ('/users/')

@app.route('/users/')
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/user/new/')
def user_new():
    return render_template("create.html")

@app.route('/user/edit/<int:id>/')
def edit_user(id):
    data = {
        "id":id #need help understanding this reference
    }
    return render_template("edit_user.html", user=User.get_one(data))

@app.route('/user/update/', methods=['POST'])
def update():
    User.update(request.form) #need explanation
    return redirect('/users/')

@app.route('/user/display/<int:id>/')
def display_user(id):
    data = {
        "id":id
    }
    return render_template("display_user.html", user=User.get_one(data))

@app.route('/user/delete/<int:id>/')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/users/')
