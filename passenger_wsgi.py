#!/usr/bin/python3


import sys, os
INTERP = '/usr/bin/python3'
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

print(f"hello, executable is {sys.executable}")

# sys.path.append('sample')
from sample.app import app as application

# Uncomment next two lines to enable debugging
#from werkzeug.debug import DebuggedApplication
#application = DebuggedApplication(application, evalex=True)

#from flask import Flask
#application = Flask(__name__)

#@application.route('/')
#def index():
#	return 'Hello passenger'
