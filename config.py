class Dev(object):
	DEBUG = True
	DEVELOPMENT = True
	SECRET_KEY = 'do-i-really-need-this'
	FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
	
	#DB info
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
									DB_CHARSET)
	print(DATABASE)
	#ovo istrazi i vidi je li potrebno ti trenutno
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	