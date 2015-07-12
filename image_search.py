import urllib2
from bs4 import BeautifulSoup
import random
import re


def search_image(search_term):

    site = "http://www.google.com/search?tbm=isch&safe=strict&q=" + search_term
    print site
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

    req = urllib2.Request(site, headers=hdr)

    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
        return False

    images_page = page.read()
    parsing_page = BeautifulSoup(images_page)
    image_container = parsing_page.select("div#rg_s")[0]
    image_tags = image_container.findAll("a", {"class": "rg_l"}, limit=20)
    final = ""
    counter = 0
    while counter < len(image_tags):
        i = random.choice(image_tags)
        split_at = i["href"].find("imgurl=") + 7
        end_split = i["href"].find("&imgrefurl")
        result = i["href"][split_at:end_split]
        if result.endswith((".jpg", ".gif", ".png")):
            try_open = True
            single_image = None
            try:
                single_image = urllib2.urlopen(result)
            except:
                try_open = False
            if try_open:
                if len(BeautifulSoup(single_image).findAll(text=re.compile('404'))) > 0:
                    break
                else:
                    final = result
                    break
            else:
                pass
        counter += 1

    if final == "":
        return False
    else:
        return final

print search_image("cow")
