# Step 1: Create a virtual environment
python -m venv env

# Step 2: Activate the virtual environment
# Windows:
env\Scripts\activate
# Mac/Linux:
source env/bin/activate

# Step 3: Install Django and Django REST Framework
pip install django
pip install djangorestframework

# Step 4: Create a new Django project
django-admin startproject connectly

# Step 5: Create a new app for your API
cd connectly
python manage.py startapp api

# Step 6: Install Django REST Framework in INSTALLED_APPS
# Add 'rest_framework' to the INSTALLED_APPS section in your settings.py
