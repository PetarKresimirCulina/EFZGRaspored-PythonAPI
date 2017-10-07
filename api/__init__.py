# -*- coding: utf-8 -*-
#imports
from flask import Flask
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#app config
app = Flask(__name__)
app.config.from_object('config.Dev')

#db config
engine = create_engine(app.config['DATABASE'], echo=app.config['DB_ECHO'])
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#api - iako je ionako cijela app == api
from api.controllers.apiController import api
app.register_blueprint(api, url_prefix='/api')

#views
#ne koristi se...