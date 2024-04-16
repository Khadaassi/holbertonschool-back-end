#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch user data
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch todos for the employee
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
        todos_data = todos_response.json()

        # Count completed tasks
        completed_tasks = [todo for todo in todos_data if todo.get("completed")]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todos_data)

        # Display progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
