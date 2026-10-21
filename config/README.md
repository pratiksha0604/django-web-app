# Django Task Manager

A simple web application built with Django that lets you add tasks, mark them as done, and delete them. Tasks are stored in a database and can also be managed from the Django admin panel.

## Features

- Add new tasks from the home page
- Mark tasks as done or undo them
- Delete tasks
- Manage tasks from the Django admin
- Automated tests for the model and views

## Tech Stack

- Python 3.10+
- Django 5.2
- SQLite (default Django database)
- HTML templates with basic CSS

## Project Structure

```
django-web-app/
├── manage.py
├── requirements.txt
├── config/    (project settings and URLs)
└── core/      (models, views, urls, tests, templates)
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/pratiksha0604/django-web-app.git
cd django-web-app
```

2. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. The admin panel is at http://127.0.0.1:8000/admin/.

## Running Tests

```bash
python manage.py test
```

## Author

[pratiksha0604](https://github.com/pratiksha0604)