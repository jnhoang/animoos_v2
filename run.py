from api import create_app
import json

# instantiate app from the api.__init__ file
app = create_app()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5999', debug=True)
# this is saying if run.py (__name__) is the the starting point, then set the app object to have these settings
# i.e. not a side module called by the initial file called to run
# see this video for more info: https://www.youtube.com/watch?v=sugvnHA7ElY
