====================================
django-best-practices-template
====================================

A Django project template that follows best practices. This template is designed to be used with the `django-admin startproject <https://docs.djangoproject.com/en/5.0/ref/django-admin/#startproject/>`_ command.

Features
========

- Organized project structure
- Settings module split into base, development, and production settings
- Integration with `django-extensions <https://django-extensions.readthedocs.io/en/latest//>`_, `django-debug-toolbar <https://django-debug-toolbar.readthedocs.io/en/latest//>`_, `flake8 <https://flake8.pycqa.org/en/latest//>`_, `black <https://black.readthedocs.io/en/stable//>`_
- Includes basic setup for static files and templates

Requirements
============
- Poetry
- Django

Usage
===========

1. Create django project:

.. code-block:: console

    django-admin startproject --template=https://github.com/SolanoJason/django-best-practices-template/archive/main.zip --extension=py,toml,env projectname

.. code-block:: console

    cd projectname

2. Install dependencies using poetry

.. code-block:: console

    poetry install

3. check if everything is working fine

.. code-block:: console

    python manage.py runserver

How to start an Application inside apps/ directory
===========

1. Using manage.py:

.. code-block:: console

    cd apps/

.. code-block:: console

    python ../manage.py startapp <app_name>

2. Using django-admin:

.. code-block:: console

    mkdir apps/<app_name>

.. code-block:: console

    django-admin startapp <app_name> apps/<app_name>

Contributing
============

Contributions are welcome! Please fork the repository and submit a pull request.
