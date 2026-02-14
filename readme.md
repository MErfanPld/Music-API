## Setup ....

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/MErfanPld/Music-API
$ cd Music-API
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/schema/swagger-ui/`.


## Start Celery

```bash
$ celery -A config worker -l info

$ celery -A config beat -l info
```
