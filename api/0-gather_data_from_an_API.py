#!/usr/bin/python3
""" using this REST API """

import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
        sys.exit(1)

    id = sys.argv[1]

    """ check user's information """
    employee = requests.get(API_URL + "users/{}".format(id)).json()

    """ check user's to do list """
    todo_list = requests.get("{}todos?userId={}".format(API_URL, id)).json()

    """ filter for task complete """
    completed_tasks = [task.get("title")
                       for task in todo_list if task.get("completed") is True]

    """ display progression """
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed_tasks), len(todo_list)))

    for task in completed_tasks:
        print("\t {}".format(task))