from api import app

app.config.from_object('config.Dev')

if __name__ == '__main__':
	app.run('0.0.0.0')

