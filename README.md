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



### -----------------------------------
### 5. DJANGO MODEL, VIEW & TEMPLATE
### -----------------------------------


#### 5.1.16 Concept Model, View and Template


                                        |-- > Model
                                        |
        |USER|--- > URL ---- > View ----|
                                        |   
                                        |-- > Template


#### 5.2.17 Setting up static file and template directories

        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

        modified:   README.md
        modified:   config/settings.py

#### 5.3.18 Adding static files and html templates
 
        modified:   .gitignore
        modified:   README.md
        new file:   _docs/static/css/main.css
        new file:   _docs/static/images/boy.png
        new file:   _docs/static/images/girl.png
        new file:   _docs/templates/detail.html
        new file:   _docs/templates/index.html
        new file:   _docs/templates/search.html
        new file:   static/css/main.css
        new file:   static/images/boy.png
        new file:   static/images/girl.png
        new file:   templates/detail.html
        new file:   templates/index.html
        new file:   templates/search.html

#### 5.4.19 Rendering the home page 

        modified:   README.md
        new file:   apps/contact/urls.py
        modified:   apps/contact/views.py
        modified:   config/urls.py

#### 5.5.20 Loading static files

        modified:   README.md
        ...
        new file:   static/fonts/slick.woff
        modified:   templates/index.html

#### 5.6.21 Template inheritance for home page

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/index.html


#### 5.7.22 Creating search and detail pages

        modified:   README.md
        modified:   templates/detail.html
        modified:   templates/index.html
        modified:   templates/search.html

#### 5.8.23 Create Contact model and setup media files

        modified:   apps/contact/models.py
        modified:   config/settings.py

#### 5.9.24 Run migration and add some contacts        

        modified:   README.md
        modified:   apps/contact/admin.py
        new file:   apps/contact/migrations/0001_initial.py
        modified:   apps/contact/models.py
        new file:   media/images/boy.png
        new file:   media/images/girl.png

#### 5.10.25 Customizing Admin panel

        modified:   README.md
        modified:   config/urls.py

#### 5.11.26 Removing Group models from admin

        modified:   README.md
        modified:   apps/contact/admin.py

#### 5.12.27 Customizing List disply and filter in Admin panel

        modified:   README.md
        modified:   apps/contact/admin.py

#### 5.13.28 Rendering data from views to template

        modified:   README.md
        modified:   apps/contact/views.py
        modified:   templates/index.html

#### 5.14.29 Jinja 2 Syntax 

        # 1. Basic configuration
        {% ... %} for statements
        {{ ... }} for expressions to print output in template
        {# ... #} for comments

        # 2. Conditional Rendering
        {% if expression %}
        ...
        {% elif expression %}
        ...
        {% else %}
        ...
        {% endif %}

        # 3. Looping using for loop
        {% for item in items %}
        ...
        {% endfor %}

        modified:   README.md




























































































































































