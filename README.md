# Decsription
    This is an ecommerce platform that use django Rest Framework 

# Project Setup

## Create the project directory
    mkdir tutorial
    cd tutorial

## Create a virtual environment to isolate our package dependencies locally
    python3 -m venv env
     env\Scripts\activate

## Install Django and Django REST framework into the virtual environment
    pip install djangorestframework

## Set up a new project with a single application
    django-admin startproject tutorial . 
    cd tutorial
    pytho manage.py startapp quickstart
    
## migrate
    python manage.py migrate

## Create a superuser
    python manage.py createsuperuser --username beth --email admin@example.com

## Create a views.py
    tutorial/quickstart/views.py

## Create URLS.py
    tutorial/urls.py

## Configure the settings.py
    REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
         INSTALLED_APPS = [
            ...
            'rest_framework',
         ]

# Testing our API
    python manage.py runserver
    
    
# Creating  the models of our ecommerce
   tutorial/quickstart/views.py
    
 
 
    






   

    
    
 
