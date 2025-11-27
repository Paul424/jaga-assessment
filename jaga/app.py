import os
from flask import Flask, url_for, session
from flask import render_template, redirect
from .views import register_views

# Create and configure the app
app = Flask(__name__, instance_relative_config=True)

# Hard coded defaults
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'jaga.sqlite'),
)

# Load app defaults from config.py
app.config.from_object('jaga.config')

# Optionally load and override configuration from a py file pointed to by an env
if 'APP_CONFIG' in os.environ:
    app.config.from_envvar('APP_CONFIG')

# Ensure the instance folder exists
app.logger.debug(f'Configured instance path {app.instance_path}')
if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)

# Register the views recursively
register_views(app)
