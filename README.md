# jaga-assessment

A small / simple Flask application to retrieve and manage tasks

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

```
# Using internal debug server
cd jaga
flask --app app run --debug

# On another shell
curl -XPOST http://localhost:5000/tasks/ -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"fred", "email":"fred.flintstone@gmail.com"}'
curl -XPOST http://localhost:5000/tasks/ -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"barney", "email":"barney.rubble@gmail.com"}'
curl -XGET http://localhost:5000/tasks/
curl -XGET http://localhost:5000/tasks/1
curl -XPUT http://localhost:5000/tasks/2 -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"wilma", "email":"wilma.flintstone@gmail.com"}'
curl -XGET http://localhost:5000/tasks/2
curl -XDELETE http://localhost:5000/tasks/2
```

## Build (image)

## Run (compose)

## Run (kind)

## Todo list

- paging
- filtering
- sorting
- type annotations and linting
- add auth (start /w internal user model + fixture?)
- add docker file (needs uwsgi setup; gunicorn known...)
- github actions for build (multi stage to include test)
- replace sqlite with postgres (or behind an abstraction)
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
