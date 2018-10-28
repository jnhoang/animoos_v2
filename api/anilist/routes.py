import json
from flask import Blueprint

# project imports
from api.utils              import logging
from api.anilist.controller import Anilist_Controller


anilist    = Blueprint('anilist', __name__)
controller = Anilist_Controller()


@anilist.route('/api/anilist/', methods=['GET'])
def anilist_lifecheck():
  logging.info('anilist lifecheck received request')

  return 'success', 200

@anilist.route('/api/anilist/browse/', methods=['GET'])
def get_browse():
  logging.info('received request to get all browse data')
  foo = controller.get_browse()
  return foo

