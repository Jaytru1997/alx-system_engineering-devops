#! /usr/bin/env python3

"""
This gives an employees todo
with some id
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])
    # employee_id = int(input('Enter Employee ID: '))

    todo = requests.get("{}todos?userId={}".format(url, employee_id))
    user = requests.get("{}users?id={}".format(url, employee_id))

    todo_lst = todo.json()
    EMPLOYEE_NAME = user.json()[0].get("name")

    # print(todo_lst, name)

    str_format = "Employee {} is done with tasks({}/{}):\n"
    todo_str = ""
    total = len(todo_lst)
    done = 0
    for todo in todo_lst:
        if todo.get("completed"):
            done += 1
            todo_str += "\t " + todo.get("title") + "\n"

    print(str_format.format(EMPLOYEE_NAME, done, total) + todo_str[:-1])
