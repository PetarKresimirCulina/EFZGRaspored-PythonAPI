class Base(object):
    DEBUG = False
    DEVELOPMENT = False
    DB_ECHO = False
    SECRET_KEY = 'P7EYX3fpih6CG2vbWXZcuJZSakug1FzaeFOmJsyrUUOhhfymKWbPo4tDMfdl'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    
class Development(Base):
    DEBUG = True
    DEVELOPMENT = True
    DB_ECHO = True
    
    DB_TYPE = 'mysql'
    DB_HOST = 'localhost'
    DB_NAME = 'wise'
    DB_CHARSET = 'utf8'
    DB_USER = 'test'
    DB_PASS = 'root'
    
    DATABASE='{0}://{1}:{2}@{3}/{4}?charset={5}'.format(
        DB_TYPE, 
        DB_USER, 
        DB_PASS, 
        DB_HOST, 
        DB_NAME, 
        DB_CHARSET
    )

class Production(Base):
    DEBUG = False
    DEVELOPMENT = False
    DB_ECHO = False
    
    DB_TYPE = 'mysql'
    DB_HOST = 'localhost'
    DB_NAME = 'wise'
    DB_CHARSET = 'utf8'
    DB_USER = 'test'
    DB_PASS = 'root'
    
    DATABASE='{0}://{1}:{2}@{3}/{4}?charset={5}'.format(
        DB_TYPE, 
        DB_USER, 
        DB_PASS, 
        DB_HOST, 
        DB_NAME, 
        DB_CHARSET
    )