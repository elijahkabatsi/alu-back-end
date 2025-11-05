#!/usr/bin/python3
"""
2-export_to_JSON.py
Fetches TODO list for a given employee ID and exports to JSON.
"""

import json
import requests
import sys


def export_employee_to_json(employee_id):
    """Fetch employee info and tasks, then write to JSON file."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    username = user.get("username")

    data = []
    for task in todos:
        data.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump({employee_id: data}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_employee_to_json(emp_id)
