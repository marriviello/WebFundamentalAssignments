from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:random_word>')
def hi(random_word):
    return f"Hi {random_word}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    #return f"{word * num}"
    return render_template("hello.html", word=word, num=num)




# @app.route('/maria')
# def maria():
#     return "Hi, Maria!"

# @app.route('/maria')
# def maria():
#     return render_template('index.html')

# @app.route('/success')
# def success():
#     return "Success"

# @app.route('/hello/<string:banana>/<int:num>') #banana is path variable
# def hello(banana, num):
#     return f"Hello {banana * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
