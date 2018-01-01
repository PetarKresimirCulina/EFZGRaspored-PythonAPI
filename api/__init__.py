# -*- coding: utf-8 -*-
from flask import Flask
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

api = Flask(__name__)
api.config.from_object('api.config.local.Local')

engine = create_engine(api.config['DATABASE'], echo=api.config['DB_ECHO'])
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

from api.v1.routes import api as apiv1
api.register_blueprint(apiv1, url_prefix='/api/v1')

@api.route('/', methods = ['GET'])
def programs():
    return 'EFZG API'

if __name__ == "__main__":
   api.run()

