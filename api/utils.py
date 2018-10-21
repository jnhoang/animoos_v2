# using this file for anything that all parts of the app may
# need. Logging for example will be used by many individual
# modules (different route, controller,etc files) within the greater app

from werkzeug.local import LocalProxy
from flask          import current_app

logging = LocalProxy(lambda: current_app.logger)
