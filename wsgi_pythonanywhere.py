import os
import sys

# Add your project directory to the sys.path
path = '/home/monaiiam/onlineShop_django'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'A.settings'

# Set up Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()