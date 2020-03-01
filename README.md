# Graduation project

## Requirements

1. VS Code latest
2. Python LTS
3. virtualenv (pip install virtualenv)
4. django (from venv => pip install django)

## How-to

1. Install VS Code + Python + virtualenv
2. Create virtual environment (virtualenv venv)
3. Run virtual environment (venv\\Scripts\\activate.bat for Windows || source venv/Scripts/activate)
4. Install django (pip install django)
5. (optional, could be removed from settings.py) Install debug toolbar (pip install django-debug-toolbar) 
6. Run project server (cd graduationwork; python manage.py runserver)
7. Project will be available on http://127.0.0.1:8000/

## Migrations

1. Change something in models.py
2. python manage.py makemigrations
3. python manage.py migrate

## Users and passwords

`Login` == `Password` 
admin == admin 
business_manager == bm_login_1 
store_manager == sm_login_1 
merchandiser == md_login_1 
