from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    if 'user' not in session:
        return render_template('logReg.html')
    else:
        return redirect('/dashboard')

@app.route('/logReg')