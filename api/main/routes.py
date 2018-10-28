import json
import requests
from flask import Blueprint

# project imports
from api.utils import logging

main = Blueprint('main', __name__)


@main.route('/api/', methods=['GET'])
def main_lifecheck():
  logging.info('lifecheck received a request')
  sample_return_object = {
    'message':  'here is a simple object to be returned to a requester' \
                'note the backslash on the previous line is used to extend ' \
                'a multi-line comment. This object is stringified (json.dumps())' \
                'before being returned to the requester',
    'status_code': 200,
    'random_list': [0, '1', 'two', {'obj': 'whoa' }]
  }
  logging.info('returning a reponse to requester')
  return json.dumps(sample_return_object)


@main.route('/api/test', methods=['GET'])
def test_route(): 
  url       = 'https://graphql.anilist.co'
  
  # Here we define our query as a multi-line string
  query = '''
    query ($id: Int) {                      # Define which variables will be used in the query (id)
      Media (id: $id, type: ANIME) {        # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
          romaji
          english
          native
        }
        startDate {
          year
          month
          day
        }
        endDate {
          year
          month
          day
        }
        coverImage {
          large
          medium
        }
        bannerImage
        format
        type
        status
        episodes
        chapters
        volumes
        season
        description
        averageScore
        meanScore
        genres
        synonyms
        nextAiringEpisode {
          airingAt
          timeUntilAiring
          episode
        }
      }
    }
  '''

  # Define our query variables and values that will be used in the query request
  variables = {
      'id': 1
  }


  # Make the HTTP Api request
  raw_res         = requests.post(url, json={ 'query': query, 'variables': variables })
  res             = raw_res.json()
  stringified_res = json.dumps(res)
  
  print 'this is what the raw_res looks like: ', raw_res
  # the raw response is wrapped within a python object, that's why it looks like <Response [200]> when logged
  print 'to look at the response as a dict we print it like so: ', raw_res.__dict__
  print '\n\nthis is the res after formatting it with json(): ', res
  print 'this is what the res looks like after reformatting it: ', stringified_res
  return stringified_res
