'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

url = 'http://demo.codingnomads.co:8080/tasks_api/users'

body = {
    "first_name": "Jonathan",
    "last_name": "Sessions",
    "email": "jon@sessionsdev.com"
}

r = requests.post(url, json=body)

print(r.status_code)
print(r.content)