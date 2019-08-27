'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests 

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 34,
    "first_name": "Jonny",
    "last_name": "Sess",
    "email": "sessions.jonathan@gmail.com"
}

r = requests.put(url, json=body)

print(r.status_code)

print(r.content)