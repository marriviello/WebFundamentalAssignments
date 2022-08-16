from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!

app = Flask(__name__)
app.secret_key='maria' #set a secret key for security
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')	 
    
# adding this method
@app.route('/show')
def show_user():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)

