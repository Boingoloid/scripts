markup = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

import urllib2
from bs4 import BeautifulSoup
import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)


br.open('https://www.thrillist.com/entertainment/nation/best-netflix-movies-right-now')
html = br.response().read()
soup = BeautifulSoup(html, "lxml-xml")

# file = open("parseddata.txt", "wb")

with open("output.html", "wb") as file:
    file.write(html)
# soupObject = soup.__dict__


print soup.prettify()
# print soupObject
