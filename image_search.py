import urllib2
from bs4 import BeautifulSoup
import random
import json


def search_image(search_term):
    term_data = urllib2.urlopen("https://duckduckgo.com/?q="+search_term+"&format=json&pretty=1")
    info_obj = json.load(term_data)
    images = []
    if "RelatedTopics" in info_obj:
        i = 0
        while i < len(info_obj["RelatedTopics"]):
            if "Icon" in info_obj["RelatedTopics"][i]:
                if info_obj["RelatedTopics"][i]["Icon"]["URL"].endswith(".ico"):
                    pass
                else:
                    images.append(info_obj["RelatedTopics"][i]["Icon"]["URL"])
            i += 1

    if images == []:
        return False
    else:
        return random.choice(images)
