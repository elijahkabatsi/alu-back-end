#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py
Exports all employees' TODOs in JSON format, keyed by employee ID.
"""

import json
import requests


def fetch_all_todos():
    """Fetch all users and their todos, return dictionary keyed by user ID."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    result = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos
            if task.get("userId") == user.get("id")
        ]
        result[user_id] = user_tasks

    return result


if __name__ == "__main__":
    all_todos = fetch_all_todos()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_todos, jsonfile)
