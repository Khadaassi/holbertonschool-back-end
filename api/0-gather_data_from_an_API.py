#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID"""

import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):

    # Fetch employee name

    employee_name = requests.get(API_URL + "users/{}".format(id)).json()

    # Fetch todos for the employee
    todos_list = requests.get(API_URL + f"/todos?userId={employee_id}")
    total_num_tasks = len(todos_list)

    # Count completed tasks
    completed_tasks = [
        task for task in todos_list.json() if task.get("completed") is True
    ]
    num_completed_tasks = len(completed_tasks)

    # Display progress
    print(
        "Employee {} is done with tasks ({}/{}):".format(
            employee_name, num_completed_tasks, total_num_tasks
        )
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
