from flask_app import app
from flask_app.controllers import users_controller
from flask_app.controllers import requests_controller

if __name__ == '__main__':
    app.run(debug=True, port = 5005)