# This is a project to define a topology of meaning, to allow an agent
# to maintain context by locating itself spatially within the map.
from bottle import route, run, template
import requests
import threading

# Built ins.
import os
import sys

# Consts
port = 8080
host = '0.0.0.0'

if len(sys.argv) == 2:
	port = int(sys.argv[1])
	host = 'localhost'

if 'PORT' in os.environ:
	port = int(os.environ['PORT'])

url = 'http://%s:%s/hello/url' % (host, port)

# Define API routes.
@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

# Start webserver on a thread (not a process for Pythonista iOS security reasons).
#run(host=host, port=port)

t = threading.Thread(target=run, kwargs={'host': host, 'port': port })
t.start()

while not t.is_alive():
	pass

# Call the API.
r = requests.request('GET', url)
print(r.content)

# Wait for the webserver thread to terminate.
t.join()
