#!/usr/bin/python3
"""
Fetches and displays the TODO list progress of a given employee.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com"

# Fetch employee data
user_resp = requests.get(f"{url}/users/{emp_id}")
todos_resp = requests.get(f"{url}/todos", params={"userId": emp_id})

if user_resp.status_code != 200 or todos_resp.status_code != 200:
    print("Error: Could not fetch data from API.")
    sys.exit(1)

user = user_resp.json()
todos = todos_resp.json()

employee_name = user.get("name")
done_tasks = [task for task in todos if task.get("completed")]

print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todos)}):")

for task in done_tasks:
    print(f"\t {task.get('title')}")
