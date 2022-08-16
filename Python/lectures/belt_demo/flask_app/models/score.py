from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Scores:
    db = 'belt_demo'
    def __init__(self, data):
        self.id=data['id']
        self.team=data['team']
        self.final_score=data['final_score']
        self.info=data['info']
        self.game_date=data['game_date']
        self.user_id=data['user_id']


    @classmethod
    def get_all(cls):
        query='SELECT * FROM scores;'
        results=connectToMySQL(cls.db).query_db(query)
        games=[]
        for row in results:
            games.append(cls(row))
        return games
    
    @classmethod
    def get_one(cls,data):
        query='SELECT * FROM scores WHERE id=%(id)s;'
        results=connectToMySQL(cls.db).query_db(query,data)
        if len(results)<1:
            return False
        return cls(restults)
        #FINISH

    @classmethod
    def save(cls,data):
        query='INSERT INTO scores (team, final_score, info, game_date, user_id) VALUES (%(team)s, %(final_score)s, %(info)s, %(game_date)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query='UPDATE scores SET team=%(team)s, final_score=%(final_score), info=%(info)s, game_date=%(game_date)s, WHERE id=%(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query='DELETE FROM scores WHERE id=%(id)s;'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def game_user(cls,data):
        query='SELECT * FROM scores LEFT JOIN user ON scores.user_id = user.id WHERE scores.id=%(id)s;'
        results=connectToMySQL(cls.db).query_db(query,data)
        for row in results:
            game = cls(results[0])
            user_data={
                'id':row['user.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['user.created_at'],
                'updated_at': row['user.updated_at']
            }
            one_user=user.User(userData)
            game.user=one_user
            all_scores.append(game)
    
