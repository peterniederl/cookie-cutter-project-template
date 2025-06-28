import os
import json
import re

def validate_input(context):
    # Validate project_name
    project_name = context.get("project_name", "")
    if not isinstance(project_name, str):
        raise ValueError("project_name must be a string.")
    if len(project_name) <= 5:
        raise ValueError("project_name must be longer than 5 characters.")
    if project_name[0].isdigit():
        raise ValueError("project_name must not start with a digit.")

    # Validate email
    email = context.get("email", "")
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, email):
        raise ValueError("email must be a valid email address.")

    # Validate author_name
    author_name = context.get("author_name", "")
    if any(char.isdigit() for char in author_name):
        raise ValueError("author_name must not contain digits.")

# Try loading from the generated `cookiecutter.json` context
context_path = os.path.join(os.getcwd(), "cookiecutter.json")

if not os.path.exists(context_path):
    raise FileNotFoundError("Could not find cookiecutter.json to extract context.")

with open(context_path) as f:
    context = json.load(f)

validate_input(context)
