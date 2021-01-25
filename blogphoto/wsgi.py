"""
WSGI config for blogphoto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogphoto.settings')

# Configurando dj-static para servir arquivos estáticos em produção
application = Cling(MediaCling(get_wsgi_application()))
