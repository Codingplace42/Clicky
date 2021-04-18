import os

from django.core.wsgi import get_wsgi_application
print("HELLO WSGI")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()
