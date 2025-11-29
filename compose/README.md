# Docker-compose setup for running jaga including dependencies

This setup is specifically created to run against a postgres database and keyclock for auth.

# Run

```
# Simply up the network and services
docker compose up [-d]
```

# Test

```
curl -XPOST http://localhost:8888/tasks/ -H 'Content-Type: application/json' -H "Accept: application/json" -d '{"username":"fred", "email":"fred.flintstone@gmail.com"}'
{"email":"fred.flintstone@gmail.com","id":1,"username":"fred"}

curl http://localhost:8888/tasks/
[{"email":"fred.flintstone@gmail.com","id":1,"username":"fred"}]
```

# Interactive

You can shell into jaga to use the cli

```
docker compose exec -it jaga /bin/bash
root@6042b0ed7005:/app# flask --app jaga.app db show
```