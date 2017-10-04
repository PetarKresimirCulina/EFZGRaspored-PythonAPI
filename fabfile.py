from api import app

def start(port=5000):
	if port:
		app.run(host='0.0.0.0', port=int(port))
	else:
		app.run(host='0.0.0.0')