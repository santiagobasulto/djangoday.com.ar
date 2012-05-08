import os
import sys
import site
from os.path import dirname

from django.core.handlers.wsgi import WSGIHandler

import pinax.env

#site.addsitedir("/home/ubuntu/env/lib/python2.7/site-packages")
#sys.path.append("/home/ubuntu/djangoday.com.ar/djangoday/apps")

PROJECT_DIR = dirname(os.path.abspath(dirname(__file__)))
APP_DIR = os.path.join(PROJECT_DIR, 'apps')

sys.path.append(APP_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoday.settings'

# setup the environment for Django and Pinax
pinax.env.setup_environ(__file__)

