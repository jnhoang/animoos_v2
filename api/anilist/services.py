import requests
import json


class Anilist_Services:
  def __init__(self):
    pass

  def get_from_anilist(self, user_query='', variables={ 'id': 1 }):
    url       = 'https://graphql.anilist.co'
    
    if user_query == '':
      user_query = '''
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
      '''
    # print user_query
    # add user requested fieds to api query scheme
    query = '''
      query ($id: Int) {
        Media (id: $id, type: ANIME) { %s }
      }
    ''' % user_query
    
    # format json data in anilist scheme
    json_data = {
      'query'    : query,
      'variables': variables
    }

    raw_res = requests.post(url, json=json_data)
    return raw_res.json()
