# gathered

commands:
py manage.py startproject
py manage.py startapp

py manage.py runserver

py manage.py makemigrations
py manage.py migrate

py manage.py createsuperuser

pip install coverage
coverage run --omit='*/venv/*' manage.py test
coverage html

pip install django
pip install djangorestframework