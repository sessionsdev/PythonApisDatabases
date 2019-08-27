'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = 'http://demo.codingnomads.co:8080/tasks_api/users'

r = requests.get(base_url)

data = r.json()
emails = []

for i in data['data']:
    emails.append(i["email"])

print(emails)