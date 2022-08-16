from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key='maria secret' #set a secret key for security

#homepage display form
@app.route('/')
def home_page():
    return render_template("index.html")

#process the form upon submission
@app.route('/process', methods=['POST'])
def submit_form():
    session['form_data'] = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comments': request.form['comments']
    }
    return redirect('/results')

#have /results route display info from the form
@app.route('/results')
def results():
    user = session['form_data']
    return render_template("results.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)