# 🍽️ Recipe Project -- Django

## 📌 About the Project

Recipe Project is a web application developed using **Python** and
**Django** for managing and displaying cooking recipes in an organized
and intuitive way.

This project was built to apply backend development best practices,
including clean architecture, authentication, CRUD operations, and
REST-ready structure.

It serves as: - A backend portfolio project - A Django learning
project - A base structure for scalable web applications

------------------------------------------------------------------------

## 🚀 Features

-   ✅ Recipe listing with pagination
-   🔍 Search functionality
-   🏷️ Categories for recipes
-   🔐 User authentication (login & registration)
-   ✏️ Create, update and delete recipes (CRUD)
-   📄 Organized template structure
-   🗂️ Clean project architecture
-   🧪 Automated tests

------------------------------------------------------------------------

## 🛠 Technologies Used

### Backend

-   Python 3
-   Django
-   Django ORM

### Frontend

-   HTML5
-   CSS3
-   Django Templates

### Database

-   SQLite (default development database)
-   Compatible with PostgreSQL / MySQL

### Tools

-   Git & GitHub
-   Virtual Environment (venv)
-   Pytest / Django TestCase

------------------------------------------------------------------------

## 📂 Project Structure

    recipe-django/
    │── project/              # Main Django configuration
    │── recipes/              # Core app (recipes logic)
    │── templates/            # HTML templates
    │── static/               # Static files (CSS, images)
    │── utils/                # Utility functions
    │── manage.py             # Django CLI entrypoint
    │── requirements.txt      # Project dependencies

------------------------------------------------------------------------

## 🧑‍💻 Installation Guide

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/tscouto/recipe-django.git
cd recipe-django
```

### 2️⃣ Create a virtual environment

``` bash
python -m venv venv
```

Activate:

**Linux/macOS**

``` bash
source venv/bin/activate
```

**Windows**

``` bash
venv\Scripts\activate
```

------------------------------------------------------------------------

### 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4️⃣ Apply database migrations

``` bash
python manage.py migrate
```

------------------------------------------------------------------------

### 5️⃣ Create a superuser (admin access)

``` bash
python manage.py createsuperuser
```

------------------------------------------------------------------------

### 6️⃣ Run the development server

``` bash
python manage.py runserver
```

Access in your browser:

    http://localhost:8000/

------------------------------------------------------------------------

## 🧪 Running Tests

To execute tests:

``` bash
pytest
```

or

``` bash
python manage.py test
```

------------------------------------------------------------------------

## 📈 Future Improvements

-   Docker containerization
-   CI/CD integration
-   API version with Django Rest Framework
-   Production-ready deployment

------------------------------------------------------------------------

## 📄 License

This project is for educational and portfolio purposes.
