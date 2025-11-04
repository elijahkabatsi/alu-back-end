#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches and displays TODO list progress for a given employee ID from a REST API.
"""

import requests
import sys


def get_employee_todos(employee_id):
    """Fetch employee info and todos from JSONPlaceholder API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [t.get("title") for t in todos if t.get("completed")]

    return employee_name, done_tasks, total_tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    employee_name, done_tasks, total_tasks = get_employee_todos(emp_id)
    print(
        f"Employee {employee_name} is done with tasks("
        f"{len(done_tasks)}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task}")
