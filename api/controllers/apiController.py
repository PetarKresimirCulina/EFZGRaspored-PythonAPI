from flask import Blueprint, current_app
from api.models import TBBranch
from flask_sqlalchemy import SQLAlchemy


api = Blueprint('api', __name__)

# Ovo su API rute - POST po defaultu makar nema smisla, trebalo bi Android app prebaciti da koristi GET radje - kasnije

@api.route('/')
def index():
	branches = TBBranch.query.all()
	for b in branches:
		print b.Name
	return 'API is here lolz' + branches[0].Name