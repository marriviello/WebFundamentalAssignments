from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos=Dojo.get_all())

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def display_dojo(id):
    data = {
        'id': id
    }
    return render_template('ninjas.html', dojo=Dojo.get_dojo_ninjas(data))
