from os import environ

from django.core.asgi import get_asgi_application
import django
import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
import signal
from hypercorn.middleware import DispatcherMiddleware

environ.setdefault("DJANGO_SETTINGS_MODULE", "mighty_meadow.settings")
django.setup()
shutdown_event = asyncio.Event()

def _signal_handler(*_):
        shutdown_event.set()

application = get_asgi_application()
