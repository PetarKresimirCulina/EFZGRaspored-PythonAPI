# -*- coding: utf-8 -*-
from api import api

def start(port=5000):
	api.run(host='0.0.0.0', port=int(port))