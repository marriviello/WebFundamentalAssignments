from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user

bcrypt=Bcrypt(app)

class Recipe:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date_cooked=data['date_cooked']
        self.thirty_min=data['thirty_min']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id = data['user_id']
        self.recipes=[]

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id=recipes.user_id;"
        results = connectToMySQL('recipes').query_db(query)
        recipes=[]
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one_recipe(cls,data):
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL('recipes').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def save_recipe(cls,data):
        query="INSERT INTO recipes (name, description, instructions, date_cooked, thirty_min, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(thirty_min)s, %(user_id)s);"
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def delete_recipe_by_ID(cls,recipe_id):
        data={
            "id": recipe_id
        }
        print("recipe id", data)
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def get_recipe_id(cls, recipe_id):
        data = {"id": recipe_id}
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query,data)
        recipe = cls(result[0])
        recipe.user = user.User.get_user_id(result["user_id"])
        return recipe

    # @classmethod
    # def get_all(cls, data):
    #     query="SELECT * FROM users LEFT JOIN recipes on users.id=recipes.user_id WHERE users.id=%(id)s;"
    #     results=connectToMySQL('recipes').query_db(query,data)
    #     user_recipe=cls(results[0])
    #     for row in results:
    #         one_recipe={
    #             'id':row['users.id'],
    #             'first_name':row['']
    #         }

    @classmethod
    def update_recipe(cls, data):
        if not cls.validate_recipe(data):
            return False
        query="UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, thirty_min=%(thirty_min)s WHEREid=%(id)s;"
        return connectToMySQL('recipes').query_db(query,data)


    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Recipe description must be at least 3 characters.")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if len(recipe['date_cooked']) <= 0:
            flash("Date cooked is required.")
            is_valid=False
        if "thirty_min" not in recipe:
            flash("Does your recipe take less than 30 min?")
            is_valid=False
        return is_valid
