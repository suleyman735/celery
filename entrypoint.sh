#!/bin/bash

echo "Apply database migrations"
python manage.py migrate

# # Check if arguments are provided
if [ "$#" -eq 0 ]; then
    echo "No command provided. Exiting."
    exit 1
fi

# Check if the command is not a directory
if [ -d "$1" ]; then
    echo "The provided command is a directory. Please provide a valid command to execute."
    exit 1
fi

# ./entrypoint.sh celery -A celery worker -l=info

exec celery "$@"
