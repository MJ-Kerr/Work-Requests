from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash 
import re
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# ==============USER CLASS=================
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ==============Create User=================
    @classmethod
    def create_user(cls, data):
        query = """
            INSERT INTO users
                ( first_name, 
                last_name, 
                email, 
                password)
            VALUES
                (%(first_name)s, 
                %(last_name)s, 
                %(email)s, 
                %(password)s);
            """
        return connectToMySQL(DATABASE).query_db(query, data)

# ==============Get A User=================
    @classmethod
    def get_user(cls, id):
        data = {
            "id": id
        }
        query = """
            SELECT * FROM users 
            WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        return User(results[0])

# =====================Get User By Email==================
    @classmethod
    def get_user_by_email(cls, email):
        data = {
            "email": email
        }
        query = """
            SELECT * FROM users 
            WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if len(results) < 1:
            return False
        return User(results[0])

# =============Validations==================
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['first_name']) == 0:
            is_valid = False
            flash('First Name is required','reg')
        if len(data['last_name']) == 0:
            is_valid = False
            flash( 'Last Name is required','reg')
        if not EMAIL_REGEX.match(data['email']):
            flash( 'Email is invalid','reg')
            is_valid = False
        else:
            future_user = User.get_user_by_email(data['email'])
            if future_user:
                is_valid = False
                flash("Email is already in use",'reg')
        if len(data['password']) < 8:
            is_valid = False
            flash('Password must be at least 8 characters long','reg')
        elif not data['password'] == data['confirm_password']:
            is_valid = False
            flash('Passwords do not match','reg')
        
        return is_valid