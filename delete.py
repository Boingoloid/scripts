# from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.shortcuts import get_list_or_404, get_object_or_404, render
import tweepy
import json, httplib
import urllib
from lxml import html
import requests
from imdbpie import Imdb
import codecs
import socket


PARSE_APP_ID = 'lzb0o0wZHxbgyIHSyZLlooijAK9afoyN8RV4XwcM'
PARSE_SECRET = 'tHZLsIENdHUpZXlfG1AZVLXsETYbgvr5lUorFegP'
PARSE_SERVER_URL = 'https://ptparse.herokuapp.com/parse'
PARSE_REST_KEY = 'YTeYDL8DeSDNsmZT219Lp8iXgPZ24ZGu3ywUjo23'


import urllib2
from base64 import b64decode, b64encode
from PIL import Image, ImageFilter

import random, string

def delete_program(id):
    print len(id)
    def delete_document(id):

        # get image url for deletion


        import json,httplib
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('DELETE', '/1/classes/GameScore/Ed1nuqPvcm', '', {
               "X-Parse-Application-Id": "${APPLICATION_ID}",
               "X-Parse-REST-API-Key": "${REST_API_KEY}"
             })
        result = json.loads(connection.getresponse().read())
        print result


        connection = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
        connection.connect()
        connection.request('POST', request_encoded, open('000001.jpg','rb').read(), {
            "X-Parse-Application-Id": PARSE_APP_ID,
            "X-Parse-REST-API-Key": PARSE_REST_KEY,
            "Content-Type": "image/jpeg"
        })
        result = json.loads(connection.getresponse().read())
        print "save image result:", result
        return result

    delete_result = delete(id)


delete_program('')



