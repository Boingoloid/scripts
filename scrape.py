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


# from matplotlib import pyplot as plt

# from django.shortcuts import render
# from django.conf import settings
# settings.configure()

PARSE_APP_ID = 'lzb0o0wZHxbgyIHSyZLlooijAK9afoyN8RV4XwcM'
PARSE_SECRET = 'tHZLsIENdHUpZXlfG1AZVLXsETYbgvr5lUorFegP'
PARSE_SERVER_URL = 'https://ptparse.herokuapp.com/parse'
PARSE_REST_KEY = 'YTeYDL8DeSDNsmZT219Lp8iXgPZ24ZGu3ywUjo23'


def home(images):
    # userDict = dict()
    # userDict['users'] = User.objects.all()
    return render(images, 'home.html')

imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests
# code_array = ['tt0479044','tt0497116','tt1286537']
# code_array = ['tt5895028','tt5929776','tt2545118']
# code_array = ['tt3530232','tt1566648','tt1355640']
# code_array = ['tt1558250','tt2381335','tt5056416']
code_array = ['tt5650594','tt1778338','tt2795078']

# code_array = ['']
print "Starting Scrape"



# title = item.title
# type = item.type
# year = item.year
# poster_url = item.poster_url
# runtime = item.runtime
# genres = item.genres
# imdb_id = item.imdb_id
# plot_outline = item.plot_outline
# plots = item.plots



import urllib2
from base64 import b64decode, b64encode
from PIL import Image, ImageFilter


import random, string
# password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

def go(code):
    item = imdb.get_title_by_id(code)

    imageTry = urllib2.urlopen(item.poster_url).read()
    encoded_data = b64encode(imageTry)

    URL = item.poster_url
    image_file = urllib.urlretrieve(URL, "000001.jpg")
    img = Image.open("000001.jpg")

    # sock.settimeout(0.0)

    # request_path = item.title.replace(":", "")
    # request_path = "/parse/files/poster_url_" + request_path.replace (" ", "_") + ".jpg"
    request_path = "/parse/files/poster_url.jpg"
    request_encoded = request_path.encode('utf-8')

    def save_image_imdb(image_file):
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

    def save_imdb_documentary(item,image_save_result):

        item_dictionary = item.__dict__
        imdb_dictionary = str(item_dictionary)

        connection2 = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
        connection2.connect()
        connection2.request('POST', '/parse/classes/Programs', json.dumps({
            "programTitle": item.title,
            "programDescription": item.plot_outline,
            "type": item.type,
            "tagCustom": "documentary",
            "posterURL": URL,
            "programImage": {
                     "name": image_save_result['name'],
                     "url:": image_save_result['url'],
                     "__type": "File"
                   },
            "imdbDictionary": imdb_dictionary,
            "imdbId": code
            }), {
            "X-Parse-Application-Id": PARSE_APP_ID,
            "X-Parse-REST-API-Key": PARSE_REST_KEY,
            "Content-Type": "application/json"
        })
        result = json.loads(connection2.getresponse().read())
        print "save imdb doc result:", result
        return result

    def save_imdb_documentary_no_image(item):

        item_dictionary = item.__dict__
        imdb_dictionary = str(item_dictionary)

        connection2 = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
        connection2.connect()
        connection2.request('POST', '/parse/classes/Programs', json.dumps({
            "programTitle": item.title,
            "programDescription": item.plot_outline,
            "type": item.type,
            "tagCustom": "documentary",
            "posterURL": URL,
            "imdbDictionary": imdb_dictionary,
            "imdbId": code
            }), {
            "X-Parse-Application-Id": PARSE_APP_ID,
            "X-Parse-REST-API-Key": PARSE_REST_KEY,
            "Content-Type": "application/json"
        })
        result = json.loads(connection2.getresponse().read())
        print "save imdb doc result:", result
        return result

    def copy_programid_to_segmentid(object_id):
        connection3 = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
        connection3.connect()
        connection3.request('PUT', '/parse/classes/Programs/' + str(object_id), json.dumps({
            "segmentId": object_id,
            "programId": object_id
            }), {
            "X-Parse-Application-Id": PARSE_APP_ID,
            "X-Parse-REST-API-Key": PARSE_REST_KEY,
            "Content-Type": "application/json"
        })
        result = json.loads(connection3.getresponse().read())
        print "save copy id result:", result
        return result

    try:
        image_save_result = save_image_imdb(item)
        save_result = save_imdb_documentary(item,image_save_result)
    except:
        save_result = save_imdb_documentary_no_image(item)

    object_id = save_result['objectId']
    edit_result = copy_programid_to_segmentid(object_id)

print len(code_array)

for code in code_array:
    go(code)









# print imdb.search_for_title("The Dark Knight")

# home(data)


# # print imdb.search_for_title("The Dark Knight")
# 
# title = imdb.get_title_by_id("tt1210166")
# print title.trailer_image_urls
# 
# data = imdb.get_title_images("tt1210166")
# 
# import PIL.Image
# img = PIL.Image.open(data)
# img.show()



# pil_im = Image.open(data[0]["Image"])


# plt.imshow(data, interpolation='nearest')
# plt.show()
# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.content)
# # print tree
# 
# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')
# 
# print 'Buyers: ', buyers
# print 'Prices: ', prices