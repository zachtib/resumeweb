import os
import sys

for path in ('/usr/local/django-apps/', '/usr/local/django-apps/resumeweb'):
    if path not in sys.path:
            sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'resumeweb.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

