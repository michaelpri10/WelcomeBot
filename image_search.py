import urllib2
from BeautifulSoup import BeautifulSoup

def search_image(string):
	url = 'https://duckduckgo.com/?q='+string+'&iax=1&ia=images' #DuckDuckGO!!!!!!
	socket = urllib2.urlopen(url)
	HTMLdata = socket.read()
	socket.close()
	parsed_html = BeautifulSoup(HTMLdata)
	return parsed_html.find('tile--img__img')['src']
	


