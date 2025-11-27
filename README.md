# jaga-assessment

A small / simple Flask application to retrieve and manage tasks

## Setup

```
conda create --name java python=3.14
conda activate java
```

## Install

```
# Install the project in the active venv (in development mode)
pip install -e .
```

## Run (sandbox)

```
# Using internal debug server
cd jaga
flask --app app run --debug
```

## Build (image)

## Run (compose)

## Run (kind)

## Todo list

- initial setup of the app; run using internal debug server using a venv (conda)
- add db (sqlite for first tests)
- add crud+l views
- add first unittests
- paging
- filtering
- sorting
- type annotations and linting
- add auth (start /w internal user model + fixture?)
- add docker file (needs uwsgi setup; gunicorn known...)
- github actions for build (multi stage to include test)
- docker-compose /w postgresql
- add helm chart
- add kind setup /w postgresql for now simply expose rest svc and add some dummy tests in readme
- setup Azure account + oauth2 client + app domain + devops pipeline (all bonus)

refs:
- https://docs.authlib.org/en/latest/client/flask.html
- https://github.com/authlib/demo-oauth-client/blob/master/flask-google-login/app.py
- https://stackoverflow.com/questions/75652936/how-to-unit-test-that-a-flask-apps-routes-are-protected-by-authlibs-resourcepr
- liefst heb ik oauth2 oidc tegen keycloak onder compose / kind want dan werkt het voor ieder; zonder google/gh confs
- production / staging is dan tegen Azure AD (andere client conf)
- in unittest redirect aftesten en token fetch mocken tbv bypass
