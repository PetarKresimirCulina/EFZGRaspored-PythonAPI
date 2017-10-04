from flask import Blueprint, current_app, request, jsonify
from sqlalchemy import asc, desc
from api.models import TBBranch, TBProgram, db_session

api = Blueprint('api', __name__)

@api.route('/')
def index():
	branches = TBBranch.query.all()
	for b in branches:
		print b.Name
	return 'API is here lolz' + branches[0].Name

@api.route('/programs', methods = ['GET'])
def programs():
	programs = db_session.query(TBProgram).all()
	return 'works' + programs[0].Name