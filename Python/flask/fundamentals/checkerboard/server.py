from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",row=8, col=8,color_one="red", color_two="black")

@app.route('/<int:row>')
def update_rows(row):
    return render_template("index.html",row=row,col=8,color_one="red", color_two="black")

@app.route('/<int:row>/<int:col>')
def update_both(row,col):
    return render_template("index.html",row=row,col=col,color_one="red", color_two="black")

# @app.route('/<int:row>/<int:col>/<string:one>/<string:two>')
# def update_all(row,col,one,two):
#     return render_template("index.html",row=row,col=col,color_one=one, color_two=two)

if __name__=="__main__":
	app.run(debug=True)