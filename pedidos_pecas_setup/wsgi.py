import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pedidos_pecas_setup.settings')

application = get_wsgi_application()
