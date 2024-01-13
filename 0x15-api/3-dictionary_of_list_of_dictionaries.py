#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()
    new_dict = {}
    for j in data2:
        row = []
        for i in data:
            temp_dict = {}
            if j['id'] == i['userId']:
                temp_dict['username'] = j['username']
                temp_dict['task'] = i['title']
                temp_dict['completed'] = i['completed']
                row.append(temp_dict)
        new_dict[j['id']] = row
    with open("todo_all_employees.json",  "w") as json_file:
        json_obj = json.dumps(new_dict)
        json_file.write(json_obj)
