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
6. Install django-google-charts and trailling modules (pip install django-google-charts, pip install django-qsstats-magic, pip install python-dateutil)
7. Run project server (cd graduationwork; python manage.py runserver)
8. Project will be available on http://127.0.0.1:8000/

## Migrations

1. Change something in models.py
2. python manage.py makemigrations automated_system
3. python manage.py migrate

## DB diagram

```
python manage.py graph_models -a -o myapp_models.png
```

## Debug on mobile

```
python manage.py runserver 0.0.0.0:8000
```

## Users and passwords

`Login` == `Password`  
admin == admin  
manager == manager  
regular1 == regular1  
regular2 == regular2  
regular3 == regular3  
regular4 == regular4  
