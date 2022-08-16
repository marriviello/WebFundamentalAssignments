from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app import app
from flask_app.models.user import User

#Recipes Homepage
@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data={
            'id': session['user_id']
        }
        user=User.get_user_id(data)
        recipes=Recipe.get_all_recipes()

        return render_template("recipes.html", user=user, recipes=recipes)

#Create Recipe Page
@app.route('/recipes/new')
def new_recipe():
    if "user_id" not in session:
        return redirect('/')
    return render_template("create_recipe.html")

#Specific Recipe Info
@app.route('/recipes/<int:recipe_id>')
def show_recipe(recipe_id):
    if "user_id" not in session:
        return redirect('/')
    data={
        'id': recipe_id
    }
    data_user={
        'id': session['user_id']
    }
    user=User.get_user_id(data_user)
    recipe=Recipe.get_one_recipe(data)
    return render_template("show_recipe.html", user=user, recipe=recipe)

#Edit Specific Recipe
@app.route('/recipes/edit/<int:recipe_id>')
def recipe_edit_page(recipe_id):
    recipe=Recipe.get_recipe_id(recipe_id)
    return render_template ("edit_recipe.html", recipe=recipe)

#Delete Recipe
@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    Recipe.delete_recipe_by_ID(recipe_id)
    return redirect("/recipes")



##POST METHODS##

#Create recipe
@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data={
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'thirty_min': request.form['thirty_min'],
        'user_id': session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect ('/recipes')

# Edit recipe
@app.route('/recipe/update/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    Recipe.update_recipe(request.form, session['user_id'])
    return redirect("/recipes/{{recipe_id}}")