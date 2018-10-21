from flask import Flask

from api.config import Config


# initialize app extensions here


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
  from api.main.routes import main

  app.register_blueprint(main)

  print 'created app, starting now'

  return app

