from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key='maria secret' #set a secret key for security

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/') #use redirect when manipulating data

if __name__ == "__main__":
    app.run(debug=True)