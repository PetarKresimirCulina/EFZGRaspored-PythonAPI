from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#controllers
from api.controllers.apiController import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

db = SQLAlchemy(app)