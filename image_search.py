import urllib2
from html.parser import HTMLParser
from html.entities import name2codepoint

class parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("attr:", attr)


def search_image(string):
	url = 'https://www.google.com/search?tbm=isch&q='+string # write the url here
	socket = urllib2.urlopen(url)
	HTMLdata = socket.read()
	socket.close()
	parser = parseHTML()
	


