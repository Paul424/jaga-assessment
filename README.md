# jaga-assessment

A small / simple Flask application to retrieve and manage tasks

## Setup

```
conda create --name java python=3.14
conda activate java
```

## Todo list

- initial setup of the app; run using internal debug server using a venv (conda)
- add db (sqlite for first tests)
- add crud+l views
- add first unittests
- paging
- filtering
- sorting
- add auth (start /w internal user model + fixture?)
- add docker file (needs uwsgi setup; gunicorn known...)
- github actions for build (multi stage to include test)
- docker-compose /w postgresql
- add helm chart
- add kind setup /w postgresql for now simply expose rest svc and add some dummy tests in readme
- setup Azure account + oauth2 client + app domain + devops pipeline (all bonus)
