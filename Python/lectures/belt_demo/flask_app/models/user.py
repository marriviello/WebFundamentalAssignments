from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class User:
    db = 'belt_demo'
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
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos=[]
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def save_dojo(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def delete_dojo(cls,data):
        query="DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod