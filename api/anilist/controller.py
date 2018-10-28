from api.anilist.services import Anilist_Services
import json

class Anilist_Controller:
  def __init__(self):
    self.services = Anilist_Services()

  def get_browse(self):
    foo = json.dumps(self.services.get_from_anilist())
    return json.dumps(foo)
    
    # validate request

    # forward request to anilist

    # format response

    # return response to request
