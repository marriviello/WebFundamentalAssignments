from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_reg_assignment').query_db(query)
        users=[]
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL('login_reg_assignment').query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('login_reg_assignment').query_db(query,data)

    @classmethod
    def user_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL('login_reg_assignment').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_user_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_reg_assignment').query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete(cls,data):
        query="DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('login_reg_assignment').query_db(query,data)

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        query="SELECT * FROM users WHERE email=%(email)s;"
        results=connectToMySQL('login_reg_assignment').query_db(query,user)
        if len(results) >= 1:
            flash("That email is already in our system")
            is_valid= False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['password'] != user['verify_password']:
            flash("Passwords don't match")
            is_valid=False
        return is_valid