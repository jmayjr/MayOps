import dotenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

"""
WSGI config for May_Ops project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'May_Ops.settings')

application = get_wsgi_application()
