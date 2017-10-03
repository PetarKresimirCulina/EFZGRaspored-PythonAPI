class Dev(object):
	DEBUG = True
	DEVELOPMENT = True
	SECRET_KEY = 'do-i-really-need-this'
	FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
	SQLALCHEMY_DATABASE_URI='mysql://test:root@localhost/wise'
	#ovo istrazi i vidi je li potrebno ti trenutno
	SQLALCHEMY_TRACK_MODIFICATIONS = False