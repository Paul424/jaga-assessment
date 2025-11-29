#!/usr/bin/env bash

set -x

# Apply migrations
flask --app jaga.app db upgrade --directory /app/migrations

# Run
gunicorn -w 1 --bind 0.0.0.0:8888 "jaga.app:create_app()"
