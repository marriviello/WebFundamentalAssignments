from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]

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
    def get_dojo_ninjas(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas on dojos.id=ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo=cls(results[0])
        for row in results:
            one_ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'first_name': row['first_name'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
            }
            print ("results",results)
            dojo.ninjas.append(ninja.Ninja(one_ninja))
        return dojo
