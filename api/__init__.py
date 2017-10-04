from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Dev')

from api.controllers.apiController import api

app.register_blueprint(api, url_prefix='/api')