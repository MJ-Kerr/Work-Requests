from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_models
from flask import flash


class request:
    def __init__(self, data):
        self.request_id = data['request_id']
        self.request_name = data['request_name']
        self.home_city = data['home_city']
        self.genre = data['genre']
        self.users_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = None

    def print(self):
        print(self.request_id)
        print(self.request_name)
        print(self.home_city)
        print(self.genre)
        print(self.users_id)
        print(self.created_at)
        print(self.updated_at)
        print(self.users)

# ===================Create Sighting=====================


    @classmethod
    def create_request(cls, data):
        query = """
        INSERT INTO requests
            (home_city,
            genre,
            request_name,
            users_id)
        VALUES 
            (%(home_city)s, 
            %(genre)s,
            %(request_name)s,
            %(users_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# =================Get All requests =====================

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM requests
        JOIN users 
        ON users.id = requests.users_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        list_of_requests = []
        print(results)
        for row in results:
            this_request = cls(row)
            # create user for sighting
            user_data = {
                **row,
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = users_models.User(user_data)
            this_request.users = this_user
            list_of_requests.append(this_request)
            this_request.print()
        return list_of_requests

# ================Get Sighting=====================

    @classmethod
    def get_request(cls,id):
        data ={
            'id': id,
        }
        query = """
        SELECT * FROM requests
        JOIN users 
        ON users.id = requests.users_id
        WHERE request_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            this_request = cls(results[0])
            # create user for sighting
            user_data = {
                **results[0],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
            }
            this_user = users_models.User(user_data)
            this_request.users = this_user
            return this_request
        else:
            return False


# =================Update Sighting=====================

    @classmethod
    def update(cls, data):
        query = """
        UPDATE requests
        SET
            request_name = %(request_name)s,
            home_city = %(home_city)s, 
            genre = %(genre)s,
        WHERE request_id = %(request_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


# ================Delete Sighting=====================

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM requests
        WHERE request_id = %(request_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# ================Validate Sighting=====================
    @staticmethod
    def validate(data):
        is_valid =True

        if len(data['request_name']) == 0:
            is_valid = False
            flash('Name is required')

        if len(data['home_city    ']) == 0:
            is_valid = False
            flash('Location is required')

        if len(data['genre']) ==0 :
            is_valid = False
            flash('Genre is required')

        return is_valid
