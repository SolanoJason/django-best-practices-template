====================================
django-best-practices-template
====================================

A Django project template that follows best practices. This template is designed to be used with the `django-admin startproject <https://docs.djangoproject.com/en/5.0/ref/django-admin/#startproject/>`_ command.

Features
========

- Organized project structure
- Settings module split into base, development, and production settings
- Custom user model in the accounts app
- Integration with `django-extensions <https://django-extensions.readthedocs.io/en/latest//>`_ and `django-debug-toolbar <https://django-debug-toolbar.readthedocs.io/en/latest//>`_
- Includes basic setup for static files and templates

Requirements
============
- Poetry
- Django

Usage
===========


1. Create django project:

.. code-block:: console

    $ django-admin startproject --template=https://github.com/SolanoJason/django-best-practices-template/archive/main.zip --extension=py,toml projectname

.. code-block:: console

    $ cd projectname

2. Install dependencies using poetry

.. code-block:: console

    $ poetry install

Contributing
============

Contributions are welcome! Please fork the repository and submit a pull request.
