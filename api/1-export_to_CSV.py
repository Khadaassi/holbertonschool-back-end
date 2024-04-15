#!/usr/bin/python3
""" Export data in the CSV format """
import csv
import requests
import sys

def export_user_tasks(url):
    try:
        users = requests.get(url).json()
        for user in users:
            userId = user.get("id")
            username = user.get("username")
            todos = requests.get(url + f"/{userId}/todos").json()
            filename = f"{userId}.csv"
            with open(filename, mode='w') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                for todo in todos:
                    writer.writerow([userId, username, todo.get("completed"),
                                     todo.get("title")])
            print(f"Data for user {userId} exported to {filename} successfully.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    export_user_tasks(url)
