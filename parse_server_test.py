import json, httplib
import urllib
import urllib2
from base64 import b64decode, b64encode
import pymongo


PARSE_APP_ID = 'lzb0o0wZHxbgyIHSyZLlooijAK9afoyN8RV4XwcM'
PARSE_SECRET = 'tHZLsIENdHUpZXlfG1AZVLXsETYbgvr5lUorFegP'
PARSE_SERVER_URL = 'https://ptparse.herokuapp.com/parse'
PARSE_REST_KEY = 'YTeYDL8DeSDNsmZT219Lp8iXgPZ24ZGu3ywUjo23'

request_path = "/parse/files/poster_url.jpg"
request_encoded = request_path.encode('utf-8')


# connection = httplib.HTTPConnection('localhost', 1337)
# connection.connect()
# connection.request('POST', '/parse/classes/GameScore', '{"score":1337,"playerName":"Sean Plott","cheatMode":false}', {
#     "X-Parse-Application-Id": PARSE_APP_ID,
#     "X-Parse-REST-API-Key": PARSE_REST_KEY
# })
# result = connection.getresponse().read()
# print "save result:", result

# connection = httplib.HTTPConnection('localhost', 1337)
# connection.connect()
# connection.request('GET', '/parse/classes/', '', {
#     "X-Parse-Application-Id": PARSE_APP_ID,
#     "X-Parse-REST-API-Key": PARSE_REST_KEY
# })
# result = connection.getresponse().read()
# print "result:", result


# remove GameScore
client = pymongo.MongoClient('mongodb://localhost/test')
db = client.get_default_database()
result = db.GameScore.drop()
array = []
for doc in result:
    array.append(doc)
print array


# view all collections
# client = pymongo.MongoClient('mongodb://localhost/test')
# db = client.get_default_database()
# result = db.GameScore.find()
# array = []
# for doc in result:
#     array.append(doc)
# print array
# collection = db.collection_names(include_system_collections=True)
# for collect in collection:
#     print collect