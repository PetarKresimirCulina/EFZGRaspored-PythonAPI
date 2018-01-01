# -*- coding: utf-8 -*-
from api.config import config
class Local(config.Production):
    SECRET_KEY = "nasumičnaAlfanumeričkaVrijednostMin50Znakova"

    DB_TYPE = 'mysql'
    DB_HOST = 'localhost'
    DB_NAME = 'wise'
    DB_CHARSET = 'utf8'
    DB_USER = 'root'
    DB_PASS = 'root'
    
    DATABASE='{0}://{1}:{2}@{3}/{4}?charset={5}'.format(
        DB_TYPE, 
        DB_USER, 
        DB_PASS, 
        DB_HOST, 
        DB_NAME, 
        DB_CHARSET
    )

