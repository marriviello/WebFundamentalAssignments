from flask import Flask, render_template, redirect, session
app=Flask(__name__)
app.secret_key="secret key message"

@app.route('/home')
def index():
    home_page = render_template('index.html', people=people)
    return home_page

@app.route('/memeber/<int:id>')
def display_member(id):
    this_person = get_person_by_id(id)
    if this_person:
        return render_template('profile.html', person=this_person)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', people=people)

def get_person_by_id(id):
    for person in people:
        if person['id'] == id:
            return person

@app.route('/edit/<int:id>')
def edit_page(id):
    this_person=get_user_by_id(id)
    return render_template('edit_user.html', person=this_person)

@app.route('/edit/<int:id>/process', methods=['POST'])
def process_edit_data(id):
    session['new_data'] = {
        'name': request.form['name'],
        'gender': request.form['gender'],
        'id': request.form['id']
    }
    return redirect (f'/confirmation/{id}')

@app.route('/confirmation/<int:id>')
def compare_data():
    old_data = get_person_by_id(id)
    return render_template('confirm.html', old_data=old_data)


people = [
    {
    'id':1,
    'name': "Maria",
    'gender': "Female",
    },
    {
    'id':2,
    'name': "Harry",
    'gender': "Male",
    }
]







if __name__=="__main__":
    app.run(debug=True)