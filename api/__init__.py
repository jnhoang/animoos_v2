from flask import Flask

# logging imports
import logging
from pythonjsonlogger import jsonlogger

# project imports
from api.config import Config



# initialize app extensions here
# configure logging
formatter  = jsonlogger.JsonFormatter('(levelname), (message), (module), (asctime)')
logger     = logging.getLogger()
logHandler = logging.StreamHandler()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

# change log lvls here  ['INFO', 'DEBUG']
logger.setLevel(logging.INFO)

# Disable flask logging
logging.getLogger('werkzeug').setLevel(logging.ERROR)



# http://flask.pocoo.org/docs/0.12/patterns/appfactories/
def create_app(config_class=Config):

  # CONFIGURATION
  # http://flask.pocoo.org/docs/1.0/config/#configuration-basics
  app = Flask(__name__)
  app.config.from_object(Config)

  # EXTENSIONS
  # bind app to extensions
  # http://flask.pocoo.org/docs/1.0/extensiondev/#the-extension-code

  
  # REGISTER BLUEPRINTS (blocks of code for routes)
  from api.main.routes    import main
  from api.anilist.routes import anilist

  app.register_blueprint(main)
  app.register_blueprint(anilist)

  logging.info('created app, starting now')
  return app

