'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

import requests
import json
from pprint import pprint

base_url = "http://www.example.com"
task_list = []

def show_menu():
    pass

def create_account():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    email_add = input("Email Address: ")
    body = {
        "first_name": f_name,
        "last_name": l_name,
        "email": email_add,
        "tasks": json.dumps(task_list)
    }

    r = requests.post(base_url, json=body)


def show_task_list():
    r = requests.get(base_url)
    data = r.json()
    for i in data["data"]:
        print(i["tasks"])


def new_task():
    new_task = input("Enter your new task: ")
    task_list.append(new_task)
    new_task_list = json.dumps(task_list)
    body = {
        "tasks": new_task_list
    }
    r = requests.post(base_url, json = body)


def show_completed_tasks():
    pass

def show_incomplete_tasks():
    pass

def mark_complete():
    pass

def update_task():
    pass

def delete_task():
    pass