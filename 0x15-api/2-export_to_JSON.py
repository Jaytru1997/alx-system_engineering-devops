#!/usr/bin/python3
"""
This gives gives an employee's todo
with some id, and exports it to
csv
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    todo = requests.get("{}todos?userId={}".format(url, employee_id))
    user = requests.get("{}users?id={}".format(url, employee_id))

    todo_lst = todo.json()
    EMPLOYEE_NAME = user.json()[0].get("username")

    data = {str(employee_id): [{"task": todo.get("title"), "completed":
                                todo.get("completed"), "username":
                                EMPLOYEE_NAME} for todo in todo_lst]}

    with open("{}.json".format(employee_id), "w") as data_file:
        data_file.write(json.dumps(data))
