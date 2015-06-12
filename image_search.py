import urllib2
from bs4 import BeautifulSoup
import random

def search_image(search_term):
	HTMLdata = urllib2.urlopen("https://en.wikipedia.org/wiki/"+search_term).read() #DuckDuckGO!!!!!!
	parsed_html = BeautifulSoup(HTMLdata)
	images = parsed_html.select("a.image > img")
	image_srcs = [i['src'] for i in images]
	return "https:"+random.choice(image_srcs)
