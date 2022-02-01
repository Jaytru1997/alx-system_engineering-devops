#!/usr/bin/python3
"""
This gives gives an employees todo
with some id
"""
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])

    todo_response = requests.get("{}todos?userId={}".format(base_url, emp_id))
    user_response = requests.get("{}users?id={}".format(base_url, emp_id))

    todo_lst = todo_response.json()
    name = user_response.json()[0].get("name")

    str_format = "Employee {} is done with tasks({}/{}):\n"
    todo_str = ""
    complete = 0
    for todo in todo_lst:
        if todo.get("completed"):
            complete += 1
            todo_str += "\t " + todo.get("title") + "\n"

    print(str_format.format(name, complete, len(todo_lst)) + todo_str[:-1])
