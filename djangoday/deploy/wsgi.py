import os
import sys
from os.path import dirname

import pinax.env

#sys.path.append("/home/ubuntu/djangoday.com.ar/djangoday/apps")

PROJECT_DIR = dirname(os.path.abspath(dirname(__file__)))
APP_DIR = os.path.join(PROJECT_DIR, 'apps')

sys.path.append(APP_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoday.settings'

# setup the environment for Django and Pinax
pinax.env.setup_environ(__file__)
