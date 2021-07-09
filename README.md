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



### ------------------------------------------
### 5. DJANGO MODEL, VIEW, TEMPLATE & ADMIN
### ------------------------------------------


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



### ------------------------------------------------------
### 6. HOMEPAGE - RENDERING DATA FROM VIEWS TO TEMPLATE
### ------------------------------------------------------


#### 6.1.28 Rendering data from views to template

        modified:   README.md
        modified:   apps/contact/views.py
        modified:   templates/index.html

#### 6.2.29 Jinja 2 Syntax and modify README.md

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

#### 6.3.30 Passing contacts objects to template

        def home(request):
                context = {
                        'contacts':Contact.objects.all()
                }
                return render(request, 'index.html', context)

        # The result
        <QuerySet [<Contact: Rainy Jane>, <Contact: Joy Brown>]>

        modified:   README.md
        modified:   apps/contact/views.py
        modified:   templates/index.html

#### 6.4.31 (Part 1) Displying contacts objects in template

        modified:   README.md
        new file:   media/images/contact01.PNG
        new file:   media/images/contact02.PNG
        modified:   templates/index.html

        NOTE:
        Could not display the images due to the media file root
        did not yet setup.

#### 6.5.32 (Part 2) Displying contacts objects in template (Difining media root)

        modified:   README.md
        modified:   config/urls.py

#### 6.6.33 Setting up timezone and modify Contact model aby adding datetime

        (venv3922) λ python manage.py makemigrations
        (venv3922) λ python manage.py migrate

        modified:   README.md
        new file:   apps/contact/migrations/0002_alter_contact_date_added.py
        modified:   apps/contact/models.py
        modified:   config/settings.py

#### 6.7.34 Using include and add some more contacts

        modified:   README.md
        modified:   apps/contact/admin.py
        new file:   media/images/barack_obama.jpg
        ...
        modified:   templates/index.html
        new file:   templates/shared/_card.html



### ------------------
### 7. DETAIL PAGE
### ------------------


#### 7.1.35 Getting individual Contact object from views

        Step 1 - Showing the id of each object in admin panel from admin.py
        Step 2 - Create url for detail contact
        Step 3 - Create detail view function
        Sept 4 - Add path to the anchor tag

        modified:   README.md
        modified:   apps/contact/admin.py
        modified:   apps/contact/urls.py
        modified:   apps/contact/views.py
        modified:   templates/shared/_card.html       

#### 7.2.36 (Part 1) Showing Detail card in a template

        modified:   README.md
        modified:   apps/contact/views.py
        modified:   templates/detail.html
        modified:   templates/shared/_card.html

#### 7.3.37 (Part 2) Showing Detail card in a template - Adding conditional to the style

        <div class="card my-2 mx-2 boy-card {% if 'detail' in request.path %}max-auto w-25{% endif %}">
        # {{request.path}} ==> /detail/4

        modified:   README.md
        modified:   templates/shared/_card.html



### ----------------------
### 8. CLASS BASE VIEWS
### ----------------------


#### 8.1.38 ListView for Homepage

        modified:   README.md
        modified:   apps/contact/urls.py
        modified:   apps/contact/views.py


#### 8.2.39 DetailView for contact details

        modified:   README.md
        modified:   apps/contact/urls.py
        modified:   apps/contact/views.py



### --------------------------
### 9. SEARCH FUNCTIONALITY
### --------------------------


#### 9.1.40 Setting up search url and views

        modified:   README.md
        modified:   apps/contact/urls.py
        modified:   apps/contact/views.py
        modified:   templates/base.html

#### 9.2.41 (Part 1) Passing data from template to view

        modified:   README.md
        modified:   apps/contact/views.py
        modified:   templates/base.html
        modified:   templates/search.html

        Note:
        . It return error if no value passing to search
        . See the error bellow:

        --> search for obama
        http://127.0.0.1:8000/searc/?search_term=obama
        --> http://127.0.0.1:8000/searc/
        UnboundLocalError at /searc/
        local variable 'search_term' referenced before assignment

        Next: solving the error

#### 9.3.42 (Part 2) Passing data from template to view - Solving the error with redirect method

        modified:   README.md
        modified:   apps/contact/views.py

        NOTE:)

#### 9.4.43 Filtering objects containing search term and displaying in search page

        modified:   README.md
        modified:   apps/contact/views.py
        modified:   templates/search.html

        NOTE:
        . This only search by name.
        . Can not do, ie: search by email, or phone

        NEXT> Todo multiple searches 

#### 9.5.44 Using Q method to do complex search query

        modified:   README.md
        modified:   apps/contact/views.py

        NOTE:)

























































































