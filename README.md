# coursework-4-grade

## Requirements

1. VS Code latest
2. Python LTS
3. virtualenv (pip install virtualenv)
4. django (from venv => pip install django)

## How-to

1. Install VS Code + Python + virtualenv
2. Create virtual environment (virtualenv venv)
3. Run virtual environment (venv\\Scripts\\activate.bat for Windows || source venv/Scripts/activate)
4. Install django
5. Run project server (cd coursework; python manage.py runserver)
6. Project will be available on http://127.0.0.1:8000/

## Migrations

1. Change something in models.py
2. python manage.py makemigrations
3. python manage.py migrate
