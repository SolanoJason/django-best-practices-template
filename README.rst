============
Project Name
============

A Django project template that follows best practices. This template is designed to be used with the `django-admin startproject` command.

Features
========

- Organized project structure
- Settings module split into base, development, and production settings
- Custom user model in the accounts app
- Integration with `django-extensions` and `debug_toolbar`
- Configured for easy switching between SQLite and other databases
- Includes basic setup for static files and templates

Project Structure
=================

The project structure is organized as follows:

projectname/
├── .venv/
├── apps/
│ ├── accounts/
│ │ ├── pycache/
│ │ ├── migrations/
│ │ │ ├── init.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py
│ │ ├── tests.py
│ │ ├── views.py
│ │ ├── init.py
│ ├── init.py
├── project_name/
│ ├── pycache/
│ ├── settings/
│ │ ├── pycache/
│ │ ├── base.py
│ │ ├── development.py
│ │ ├── production.py
│ │ ├── init.py
│ ├── asgi.py
│ ├── urls.py
│ ├── wsgi.py
├── templates/
├── .editorconfig
├── .gitignore
├── db.sqlite3
├── Makefile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.rst


Quick Start
===========

1. Clone the repository:

    ```
    git clone https://github.com/SolanoJason/django-best-practices-template projectname
    cd projectname
    ```

2. Create a virtual environment and install dependencies:

    ```
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your environment-specific variables:

    ```
    SECRET_KEY=<your-secret-key>
    DEBUG=True
    ```

4. Apply migrations and run the development server:

    ```
    python manage.py migrate
    python manage.py runserver
    ```

Settings
========

The settings are divided into different modules:

- `base.py`: Contains the base settings common to all environments.
- `development.py`: Contains settings specific to the development environment.
- `production.py`: Contains settings specific to the production environment.

To use a specific settings module, set the `DJANGO_SETTINGS_MODULE` environment variable:

    ```
    export DJANGO_SETTINGS_MODULE='project_name.settings.development'
    ```

Custom User Model
=================

This template uses a custom user model located in the `accounts` app. To use it, ensure that the `AUTH_USER_MODEL` setting is set correctly in your settings:

    ```
    AUTH_USER_MODEL = 'accounts.User'
    ```

Third-Party Apps
================

- `django-extensions`: A collection of custom extensions for Django.
- `debug_toolbar`: A configurable set of panels that display various debug information about the current request/response.

Contributing
============

Contributions are welcome! Please fork the repository and submit a pull request.
