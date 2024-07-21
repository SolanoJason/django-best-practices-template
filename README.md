# django-best-practices-template

A Django project template that follows best practices. This template is designed to be used with the [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#startproject) command.

## Features

- Organized project structure
- Settings module split into base, development, and production settings
- Integration with [`django-extensions`](https://django-extensions.readthedocs.io/en/latest/), [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/latest/), [`flake8`](https://flake8.pycqa.org/en/latest/), [`black`](https://black.readthedocs.io/en/stable/)
- Includes basic setup for static files and templates

## Requirements

- Poetry
- Django

## Usage

1. Create a Django project:

    ```console
    django-admin startproject --template=https://github.com/SolanoJason/django-best-practices-template/archive/main.zip --extension=py,toml,env projectname
    ```

    ```console
    cd projectname
    ```

2. Install dependencies using poetry:

    ```console
    poetry install
    ```

3. Check if everything is working fine:

    ```console
    python manage.py runserver
    ```

## How to start an Application inside apps/ directory

1. Using manage.py:

    ```console
    cd apps/
    ```

    ```console
    python ../manage.py startapp accounts
    ```

2. Using django-admin:

    ```console
    mkdir apps/accounts
    ```

    ```console
    django-admin startapp accounts apps/accounts
    ```

## How to reference Applications

In order to import applications inside the apps/ directory, we must assume the application is in the root directory. This is achieved by adding the following line of code:

    ```python
    # settings/base.py
    sys.path.insert(0, str(BASE_DIR / 'apps'))
    ```

1. For example in `INSTALLED_APPS`:

    ```python
    # settings/base.py
    LOCAL_APPS = ['accounts']
    ```

1. For example, to import modules:

    ```python
    # settings/base.py
    from accounts import models, views, forms
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
