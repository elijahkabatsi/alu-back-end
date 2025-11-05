#!/usr/bin/python3
"""
1-export_to_CSV.py
Fetches TODO list for a given employee ID and exports to CSV.
"""

import csv
import requests
import sys


def export_employee_to_csv(employee_id):
    """Fetch employee info and tasks, then write to CSV file."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    username = user.get("username")

    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_employee_to_csv(emp_id)
