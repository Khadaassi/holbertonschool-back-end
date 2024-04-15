#!/usr/bin/python3
""" Export data in the JSON format """
import json
import requests
import sys


def export_user_tasks(url):
    try:
        users = requests.get(url).json()
        all_user_tasks = {}
        for user in users:
            userId = user.get("id")
            username = user.get("username")
            todos = requests.get(url + f"/{userId}/todos").json()
            user_tasks = [
                {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                for todo in todos
            ]
            all_user_tasks[userId] = user_tasks
        with open("todo_all_employees.json", mode="w") as file:
            json.dump(all_user_tasks, file)
        print("Data for all users exported to todo_all_employees.json " +
              "successfully.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    export_user_tasks(url)
