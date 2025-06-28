def validate_input(context):
    # your logic here

if __name__ == "__main__":
    import sys
    import os
    import json

    # Load context from environment variable if available
    context_file = os.environ.get('COOKIECUTTER_CONTEXT')
    if context_file:
        with open(context_file) as f:
            context = json.load(f)
    else:
        # fallback or raise error
        context = {}

    validate_input(context)
