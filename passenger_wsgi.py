import sys, os

INTERP = "/home/kuponia/kuponia.cl/kuponiaenv/local/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

#sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'kuponia'))
os.environ['DJANGO_SETTINGS_MODULE'] = "kuponia.settings"
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
