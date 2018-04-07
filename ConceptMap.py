# This is a project to define a topology of meaning, to allow an agent
# to maintain context by locating itself spatially within the map.
from bottle import route, run, template
import requests

# Built ins.
import os
import sys
import time
import threading

# Consts
host = 'localhost'
port = 8080

# If we've passed in a port, use that.
if len(sys.argv) == 2:
	port = int(sys.argv[1])

# Override port with environment.
if 'PORT' in os.environ:
	port = int(os.environ['PORT'])
	# TODO: HACK: We're probably on Heroku, so bind to zeros instead of localhost
	host = '0.0.0.0'

# Construct base URL for query.
url = 'http://%s:%s' % (host, port)

# Override base URL for query if in environment.
if 'URL' in os.environ:
	url = os.environ['URL']

# Append path to base URL.
url = os.path.join('%s','%s') % (url, os.path.join('hello', 'testerington'))

# Define API routes.
@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

# Start webserver on a thread (not a process for Pythonista iOS security reasons).
#run(host='0.0.0.0', port=port)
t = threading.Thread(target=run, kwargs={'host': host, 'port': port })
t.start()

# TODO: HACK: Wait for the thread to start.
while not t.is_alive():
	pass

# TODO: HACK: Seriously, wait for the server to start.
time.sleep(1)

# Call the API.
r = requests.request('GET', url)
print(r.content)

# Wait for the webserver thread to terminate.
t.join()
