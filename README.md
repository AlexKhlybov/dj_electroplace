# Internet shop of household appliances
Online store of household appliances on Django.


## Stack
* Python>3.7
* Django 2.2
* PostgreSQL
* Docker
* Docker-compose


## Environment
Env file in the root of the project and add the following (example) to it:
```
DEBUG=1
SECRET_KEY=secretsecretBigsecret

DB_ENGINE=django.db.backends.postgresql
DB_PASSWORD=post
DB_NAME=post
DB_USER=post
DB_HOST=db
DB_PORT=5432
```

## Getting started
clone:
```
$ git clone https://github.com/AlexKhlybov/dj_electroplace.git
$ cd dj_electroplace
```

This project uses `docker-compose`, let's raise our application:
```
$ docker-compose up
```

Next, let's launch another terminal and go to the container with Django:
```
$ docker exec -it elp_dja bash
```

Next, we will carry out migrations and fill the database with demo data:
```
$ python manage.py migrate
$ python manage.py loaddata mainapp/fixtures/dump_db.json
```

Next, let's stop our containers `ctr + C`.
Let's bring our application up again:
```
$ docker-compose up
```
Now you can see our application in the browser - [Home page](http://127.0.0.1:8000)


## Лицензия
MIT