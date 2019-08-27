'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''

import requests
from pprint import pprint

base_url = 'http://demo.codingnomads.co:8080/tasks_api/users'

r = requests.get(base_url)

pprint(r.status_code)
pprint(r.encoding)
pprint(r.json())