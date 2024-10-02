"""
WSGI config for setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import os
import sys

# Adicione o caminho do projeto ao sys.path
sys.path.append('/home/ec2-user/crm_projeto')

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_projeto.settings')

# Importe e chame a aplicação WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()