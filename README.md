================================
DjangoDay AR website
================================

>This website has been constructed based on the work by
>Eldarion in the DjangoCon website.
>You can take a look at the original proyect hosted in github
>[https://github.com/eldarion/djangocon.us](https://github.com/eldarion/djangocon.us)

This repository stores the DjangoDay Argentina website. This
project is open source and the license can be found in LICENSE.


Installation
============

To get setup with djangday code you must have the follow installed:

 * Python 2.6+
 * virtualenv 1.4.7+
 * C compiler (for PIL)
 * virtualenvrwapper (optional, but prefered)

Setting up environment
----------------------

Create a virtual environment where djangday dependencies will live (Using virtualenvwrapper):

    $ mkvirtualenv --no-site-packages djangday
    (djangday)$

Make the project directory your working directory::

    $ cd djangday

Install djangocon project dependencies::

    (djangday)$ pip install -r requirements/project.txt

Setting up the database
-----------------------

This will vary for production and development. By default the project is set
up to run on a SQLite database. If you are setting up a production database
see the Configuration section below for where to place settings and get the
database running. Now you can run::

    (djangday)$ python manage.py syncdb

Running a web server
--------------------

In development you should run::

    (djangday)$ python manage.py runserver

For production, this project comes with a WSGI entry point located in
``deploy/wsgi.py`` and can be referenced by gunicorn with
``deploy.wsgi:application``.

Configuration
=============

You can create a ``local_settings.py`` file alongside ``settings.py`` to
override any setting that may be environment/instance specific. This file is
ignored in ``.gitignore``.

Data configuration
------------------

Create a proposal type (@@@ change once upgraded to newer symposion)::

    >>> from symposion.proposals.models import ProposalKind
    >>> ProposalKind.objects.create(name="Test")

Issues
======

If you find an issue with this code base please fill an issue on github.
