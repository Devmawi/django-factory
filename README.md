# Django Factory

Simple project for demonstrating useful core functionality of django.
For simplicity there are some shortcuts, so don't assume this is production ready code.

## Build and debug

``` powershell
# install requirements for local development
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# add some machines at url /admin/machines
```

## Useful commnds

``` powershell
django-admin startproject django_factory
cd ./django_factory
django-admin startapp machines
python manage.py makemigrations machines
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```