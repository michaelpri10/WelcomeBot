import urllib2
from bs4 import BeautifulSoup
import random

def search_image(search_term):
    images_page = urllib2.urlopen("http://compfight.com/search/" + search_term + "/1-0-1-1")
    parsing_page = BeautifulSoup(images_page)
    image_parents = parsing_page.findAll("a", id=lambda x: x and x.startswith("photo_link_"))
    image_tags = []
    for i in image_parents:
        image_tags.append(i.find("img"))
    images = [i['src'] for i in image_tags]
    if len(images) == 0:
        return False
    else:
        return random.choice(images)
