def validate_input(context):
    assert " " not in context["cookiecutter"]["package_name"], "Package name must not contain spaces"

validate_input(context)
