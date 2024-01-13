#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TO-DO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    tasks_done = 0
    tasks_total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            employee_name = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            tasks_total += 1

            if i.get('completed') is True:
                tasks_done += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          tasks_done,
                                                          tasks_total))

    for i in tasks:
        print("\t {}".format(i))
