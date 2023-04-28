from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_models
from flask import flash


class Work:
    def __init__(self, data):
        self.work_id = data['work_id']
        self.type = data['type']
        self.description = data['description']
        self.language = data['language']
        self.users_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = None

    def print(self):
        print(self.work_id)
        print(self.type)
        print(self.description)
        print(self.language)
        print(self.users_id)
        print(self.created_at)
        print(self.updated_at)
        print(self.users)

# ===================Create Work=====================


    @classmethod
    def create_work(cls, data):
        query = """
        INSERT INTO works
            (description,
            language,
            type,
            users_id)
        VALUES 
            (%(description)s, 
            %(language)s,
            %(type)s,
            %(users_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# =================Get All works =====================

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM works
        JOIN users 
        ON users.id = works.users_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        list_of_works = []
        print(results)
        for row in results:
            this_work = cls(row)
            user_data = {
                **row,
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = users_models.User(user_data)
            this_work.users = this_user
            list_of_works.append(this_work)
            this_work.print()
        return list_of_works

# ================Get Work=====================

    @classmethod
    def get_work(cls,id):
        data ={
            'id': id,
        }
        query = """
        SELECT * FROM works
        JOIN users 
        ON users.id = works.users_id
        WHERE work_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            this_work = cls(results[0])
            # create user for work
            user_data = {
                **results[0],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
            }
            this_user = users_models.User(user_data)
            this_work.users = this_user
            return this_work
        else:
            return False


# =================Update Work=====================

    @classmethod
    def update(cls, data):
        query = """
        UPDATE works
        SET
            type = %(type)s,
            description = %(description)s, 
            language = %(language)s,
        WHERE work_id = %(work_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


# ================Delete Work=====================

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM works
        WHERE work_id = %(work_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# ================Validate Work=====================
    @staticmethod
    def validate(data):
        is_valid =True

        if len(data['type']) == 0:
            is_valid = False
            flash('Name is required')

        if len(data['description']) == 0:
            is_valid = False
            flash('Location is required')

        if len(data['language']) ==0 :
            is_valid = False
            flash('Language is required')

        return is_valid
