# GameParadise - the DataBase Driven GameShop
### INFO
It's **`How to basic project`**. It contains a basic **`Django+Postgresql`** setup.
Just a simple shop with catalog only for now(will be updated in future).
### How to Install (Windows)
• Install python (python 3.9 using in project)
• Create a virtual enviroment **`python -m venv venv`** (Windows)
• Activate venv **`source venv/Scripts/activate`**
• Install Django and pcycopg2 manually or use **`pip install -r requirements.txt`**
• Create your Django project **`django-admin startproject project_name`**
• Run Django server to make sure, that all is fine **`python manage.py runserver <port_where_to_run_server>`**
• Create your apps in project_name/ directory(to find manage.py) **`python manage.py startapp app_name`**
• Add your apps to settings.py in format **`'app_name.apps.AppNameConfig',`**
• Set up urls.py and views.py in every app(and edit them) and again run server to make sure that all is working
