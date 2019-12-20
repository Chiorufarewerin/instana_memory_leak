import os
import cherrypy

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = get_wsgi_application()

cherrypy.config.update({
    'server.socket_host': "0.0.0.0",
    'server.socket_port': 8001,
    'server.thread_pool': 1,
})

cherrypy.tree.graft(app, "/")

cherrypy.engine.start()
cherrypy.engine.block()
