# This is a project to define a topology of meaning, to allow an agent
# to maintain context by locating itself spatially within the map.
from bottle import route, run, template
import requests
import threading

# Built ins.
import os
import sys

# Define API routes.
@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

port = 8080
host = '0.0.0.0'

if len(sys.argv) == 2:
	port = int(sys.argv[1])

if 'PORT' in os.environ:
	port = int(os.environ['PORT'])
	
if 'HOST' in os.environ:
	host = os.environ['HOST']

# Start webserver on a thread (not a process for Pythonista iOS security reasons).
run(host=host, port=port)

print('hello')

#t = threading.Thread(target=run, kwargs={'host': 'localhost', 'port': port })
#t.start()

# Call the API.
#r = requests.request('GET', 'http://localhost:'+port+'/hello/python')
#print(r.content)

# Wait for the webserver thread to terminate.
#t.join()
