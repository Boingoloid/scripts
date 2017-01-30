# from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.shortcuts import get_list_or_404, get_object_or_404, render
import tweepy
import json, httplib
import urllib
from lxml import html
import requests
from imdbpie import Imdb
import codecs
import urllib2
from base64 import b64decode, b64encode
from PIL import Image, ImageFilter


PARSE_APP_ID = 'lzb0o0wZHxbgyIHSyZLlooijAK9afoyN8RV4XwcM'
PARSE_SECRET = 'tHZLsIENdHUpZXlfG1AZVLXsETYbgvr5lUorFegP'
PARSE_SERVER_URL = 'https://ptparse.herokuapp.com/parse'
PARSE_REST_KEY = 'YTeYDL8DeSDNsmZT219Lp8iXgPZ24ZGu3ywUjo23'



import json,httplib
connection = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
connection.connect()
connection.request('POST', '/parse/classes/_User', json.dumps({
       "username": "cooldude6",
       "password": "p_n7!-e8",
       "phone": "415-392-0202"
     }), {
       "X-Parse-Application-Id": PARSE_APP_ID,
       "X-Parse-REST-API-Key": PARSE_REST_KEY,
       "X-Parse-Revocable-Session": "1",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result
