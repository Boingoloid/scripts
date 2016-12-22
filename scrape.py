from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
import tweepy
import json, httplib
import urllib
from lxml import html
import requests
from imdbpie import Imdb
import codecs


# from matplotlib import pyplot as plt

from django.shortcuts import render
from django.conf import settings
settings.configure()

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
item = imdb.get_title_by_id("tt0479044")
# print dir(title)
# print (title.poster_url)


# for attr in dir(item):
#     print (attr, getattr(item, attr))

print "Separator"

# print (item.title)
# print (item.type)
# print (item.year)
# print (item.poster_url)
# print (item.runtime)
# print (item.genres)
# print (item.imdb_id)
# print (item.plot_outline)
# print (item.plots)
	
title = item.title
type = item.type
year = item.year
poster_url = item.poster_url
runtime = item.runtime
genres = item.genres
imdb_id = item.imdb_id
plot_outline = item.plot_outline
plots = item.plots


import urllib2
from base64 import b64decode, b64encode


imageTry = urllib2.urlopen(poster_url).read()
encoded_data = b64encode(imageTry)


from PIL import Image, ImageFilter
#Read image
# im = Image.open( '000001.jpg' )
# #Display image
# im.show()

URL = item.poster_url
image_file = urllib.urlretrieve(URL, "000001.jpg")
img = Image.open("000001.jpg")


print item.title

request_path = item.title.replace(":", "")

request_path = "/parse/files/poster_url_" + request_path.replace (" ", "_") + ".jpg"
request_encoded = request_path.encode('utf-8')
print request_encoded

def save_image_imdb(image_file):
    connection = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
    connection.connect()
    connection.request('POST', request_encoded, open('000001.jpg','rb').read(), {
        "X-Parse-Application-Id": PARSE_APP_ID,
        "X-Parse-REST-API-Key": PARSE_REST_KEY,
        "Content-Type": "image/jpeg"
    })

    result = json.loads(connection.getresponse().read())

    result ['program_image_url']  = result['url']
    result ['program_image_name']  = result['name']
    return result
	
image_save_result = save_image_imdb(item)
print image_save_result




def save_imdb_documentary(item,image_save_result): 
    connection = httplib.HTTPSConnection('ptparse.herokuapp.com', 443)
    connection.connect()
    connection.request('POST', '/parse/classes/Programs', json.dumps({
        "programTitle": item.title,
        "programDescription": item.plot_outline,
        "Type": item.type,
        "poster_url": URL,
        "poster_image": {
		         "name": image_save_result['program_image_name'],
		         "url:": image_save_result['program_image_url'],
		         "__type": "File"
		       }
        }), {
        "X-Parse-Application-Id": PARSE_APP_ID,
        "X-Parse-REST-API-Key": PARSE_REST_KEY,
        "Content-Type": "application/json"
    })

    result = json.loads(connection.getresponse().read())
    return result

print save_imdb_documentary(item,image_save_result)

	
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