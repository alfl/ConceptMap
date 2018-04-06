# This is a project to define a topology of meaning, to allow an agent
# to maintain context by locating itself spatially within the map.
from bottle import route, run, template
import requests

# Built in packages.
import threading
import os

# Define API routes.
@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

# Start webserver on a thread (not a process for Pythonista iOS security reasons).
t = threading.Thread(target=run, kwargs={'host': 'localhost', 'port': os.environ[‘PORT’] })
t.start()

# Call the API.
r = requests.request('GET', 'http://localhost/hello/python')
print(r.content)

# Wait for the webserver thread to terminate.
t.join()
