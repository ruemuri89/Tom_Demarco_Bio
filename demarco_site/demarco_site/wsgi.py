"""
WSGI config for demarco_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demarco_site.settings')

print("=" * 50)
print("WSGI APPLICATION STARTING")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
print(f"DEBUG: {os.environ.get('DEBUG', 'Not Set')}")
print("=" * 50)

application = get_wsgi_application()
