# django-contact-manager
This is my exercise based on the course: Django | Build &amp; Deploy Fully Featured Web Application on Udemy: https://www.udemy.com/course/draft/2180008/learn/lecture/13474898#overview

### -----------
### 1. SETUP
### -----------


#### 1.1.1 Create remote repository (Github) and local repository

        modified:   README.md 

#### 1.2.2 Create virtual environment

        λ python -m venv venv3922

#### 1.3.3 Install django

        λ venv3922\scripts\activate
        (venv3922) λ python -m pip install django
        (venv3922) λ python -m pip install --upgrade pip
        modified:   README.md


### ----------------------------
### 2. DJANGO PROJECT AND APP
### ----------------------------

#### 2.1.4 Create django project 'config'

        (venv3922) λ django-admin startproject config . 
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 2.2.5 Create django app 'apps/contact' 

        (venv3922) λ mkdir apps\contact
        (venv3922) λ python manage.py startapp contact apps\contact

        modified:   README.md
        new file:   apps/contact/__init__.py
        new file:   apps/contact/admin.py
        new file:   apps/contact/apps.py
        new file:   apps/contact/migrations/__init__.py
        new file:   apps/contact/models.py
        new file:   apps/contact/tests.py
        new file:   apps/contact/views.py

#### 2.3.6 Register app to project

        (venv3922) λ python manage.py check
        System check identified no issues (0 silenced). 

        modified:   README.md
        modified:   apps/contact/apps.py
        modified:   config/settings.py


### --------------
### 3. DATABASE
### --------------


#### 3.1.7 Create postgres database

        hp=# CREATE DATABASE django_contact_manager;
        CREATE DATABASE
        hp=#

        modified:   .gitignore
        modified:   README.md

#### 3.2.8 Install django environ

       (venv3932) λ pip install django-environ

       modified:   README.md

#### 3.3.9 Install PostgreSQL driver

       (venv3932) λ python -m pip install psycopg2-binary==2.8.6

       modified:   README.md 

#### 3.4.10 Create .env file and setup environ

       (venv3932) λ touch config\.env

        modified:   .gitignore
        modified:   README.md

#### 3.5.11 Setup .env file (adding the db credentials and SECRET_KEY)

        modified:   README.md

#### 3.6.12 Use environ in settings

       (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py

#### 3.7.13 Run migration and create superuser

        (venv3922) λ python manage.py makemigrations
        No changes detected
        (venv3922) λ python manage.py migrate 
        (venv3922) λ python manage.py createsuperuser

        modified:   README.md



### -----------------------
### 4. PROJECT STRUCTURE
### -----------------------

#### 4.1.14 Create requirements.txt file

        modified:   README.md
        new file:   requirements.txt


#### 4.2.15 Current project's structures

        .
        |-- LICENSE
        |-- README.md
        |-- apps
        |   `-- contact
        |       |-- __init__.py
        |       |-- __pycache__
        |       |-- admin.py
        |       |-- apps.py
        |       |-- migrations
        |       |-- models.py
        |       |-- tests.py
        |       `-- views.py
        |-- config
        |   |-- __init__.py
        |   |-- __pycache__
        |   |   |-- __init__.cpython-39.pyc
        |   |   |-- settings.cpython-39.pyc
        |   |   |-- urls.cpython-39.pyc
        |   |   `-- wsgi.cpython-39.pyc
        |   |-- asgi.py
        |   |-- settings.py
        |   |-- urls.py
        |   `-- wsgi.py
        |-- manage.py
        |        - requirements.txt
        `-- venv3922








































































































































































































