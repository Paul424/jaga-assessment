# jaga-assessment

A small / simple Flask application to retrieve and manage tasks

Packages used:
- [Flask](https://flask.palletsprojects.com/en/stable/) Light-weight python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for orm layer
- [marshmallow](https://marshmallow.readthedocs.io/en/latest/index.html) for serializing/deserializing and validation of models on the API
- [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/index.html) as the REST framework; to simplify writing views
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) for managing data migrations
- For the data layer either buildin [SQLite3](https://sqlite.org/) or [postgres using psycopg2](https://pypi.org/project/psycopg2/)
- [gunicorn](https://gunicorn.org/) for running our app in production
- [pytest](https://docs.pytest.org/en/stable/) for managing unittests
- [authlib](https://docs.authlib.org/en/latest/index.html) for managing OAuth2 and protecting resources we own

## Setup

```
conda create --name jaga python=3.14
conda activate jaga
```

## Install

```
# Install the project in the active venv (in development mode)
pip install -e .

# Additional test dependencies are included using:
pip install -e '.[develop]'
```

## Test

The app is bundled with unittests, run as follows using pytest:
```
pytest -v
```

## Run (sandbox)

Notice a token needs to be injected for protected views; see the auth section how to generate a token.

```
# Using internal debug server
cd jaga
flask --app app run --debug

curl -XPOST http://localhost:5000/tasks/ -H 'Authorization: Bearer xxx' -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"fred", "email":"fred.flintstone@gmail.com"}'
curl -XPOST http://localhost:5000/tasks/ -H 'Authorization: Bearer xxx' -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"wilma", "email":"wilma.flintstone@gmail.com"}'
curl -XPOST http://localhost:5000/tasks/ -H 'Authorization: Bearer xxx' -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"barney", "email":"barney.rubble@gmail.com"}'
curl -XPOST http://localhost:5000/tasks/ -H 'Authorization: Bearer xxx' -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"betty", "email":"betty.rubble@gmail.com"}'
curl -XGET http://localhost:5000/tasks/ -H 'Authorization: Bearer xxx'
curl -XGET http://localhost:5000/tasks/1 -H 'Authorization: Bearer xxx'
curl -XPUT http://localhost:5000/tasks/2 -H 'Authorization: Bearer xxx' -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"wilma", "email":"wilma.flintstone@gmail.com"}'
curl -XGET http://localhost:5000/tasks/2 -H 'Authorization: Bearer xxx'
curl -XDELETE http://localhost:5000/tasks/2 -H 'Authorization: Bearer xxx'
```

## Build and Run (image)

```
# To build and test
docker build -t jaga:0.1 --progress=plain --target test .

# To create an image for run
docker build -t jaga:0.1 --progress=plain --target run .

# Then run using
docker run -p 8888:8888 jaga:0.1

# Simple test
curl http://localhost:8888/tasks/
[]

# Or interactive
docker run -it -p 8888:8888 jaga:0.1 /bin/bash
root@ff0575736b75:/app# python
Python 3.15.0a2 (main, Nov 19 2025, 18:46:12) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from  jaga import app
>>> app = app.create_app()
```

## Run (compose)

## Run (kind)

## Auth

The REST views are protected using a required OAuth2 scope. First generate a token by logging in to the upstream idp:

    http://localhost:5000/auth/token

Then insert the Bearer token in subsequent requests:
'''
curl -XGET http://localhost:5000/tasks/2 -H 'Authorization: Bearer xxxxxx'
'''


## Todo list

- type annotations and linting
- auth
    - add keycloak to compose setup
    - move gh to azure ad
- harden image (run as non root, etc...)
- gh action docker cache setup and improve labels / tags
- add helm chart
- add kind setup /w postgresql for now simply expose rest svc and add some dummy tests in readme
- setup Azure account + oauth2 client + app domain + devops pipeline (all bonus)
- add metrics endpoint + dashboard
- multiple worker support
