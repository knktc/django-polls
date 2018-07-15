# SIMPLE DJANGO POLLS APP

## About This APP

Yet another app for <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>

This is a polls management platform built on the Django Web Framework with a vote rate limiter.

## Requirements

* Python 3.6
* Django 2.0.7
* pytz 2018.5(installed with django)

## Installation
To install this App, make sure you have **Python 3.6** installed on your OS, use the following command to check your python version:

```
python --version

# or

python3 --version
```

Create venv for this app:

```
python -m venv polls_venv
```

Active venv(and run all the following steps in this venv):

```
source polls_venv/bin/active
```

Install requirements:

```
cd polls
pip install -r requirements.txt
```

Run initialization script to create database, superuser, normal users and demo data:

```
python initialization.py
```

Run development server:

```
python manage.py runserver 8000
```

Then open your browser and visit <http://127.0.0.1:8000>.

HAVE FUN!

## Configuration

We've add some custom configs in **settings.py**:

```
# custom config starts here
# vote time interval(in seconds)
VOTE_INTERVAL = 60 * 60 * 24
```

You might need to restart devlopment server after making configuration changes.

## Screenshots

Check **misc/screenshots** for system screenshots.

## Deployment

*Working in progress...*

Using **Nginx** and **uwsgi** is recommanded.

## TODO

* Restful
* logging
* unit testing
* docker