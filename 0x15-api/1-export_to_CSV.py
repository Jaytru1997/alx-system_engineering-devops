#!/usr/bin/python3
"""
This gives gives an employee's todo
with some id, and exports it to
csv
"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    todo = requests.get("{}todos?userId={}".format(url, employee_id))
    user = requests.get("{}users?id={}".format(url, employee_id))

    todo_lst = todo.json()
    EMPLOYEE_NAME = user.json()[0].get("username")

    with open("{}.csv".format(employee_id), "w") as data_file:
        csv_writer = csv.writer(data_file,
                                quotechar='\"',
                                quoting=csv.QUOTE_ALL)
        for todo in todo_lst:
            csv_writer.writerow(
                [str(employee_id),
                 EMPLOYEE_NAME,
                 str(todo.get("completed")),
                 todo.get("title")])
