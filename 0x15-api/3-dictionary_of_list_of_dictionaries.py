#!/usr/bin/python3
"""
This gives an employee's todo
with some id, and exports it to
csv
"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get("{}users".format(url))

    data = {}
    for user in user.json():

        todo = requests.get(
            "{}todos?userId={}".format(url, user.get("id")))
        todos = todo.json()

        data[user.get("id")] = [{"task": todo.get("title"),
                                 "completed": todo.get("completed"),
                                 "username": user.get("username")}
                                for todo in todos]

    with open("todo_all_employees.json", "w") as data_file:
        data_file.write(json.dumps(data))
