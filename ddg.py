import urllib2;

def search(string):
  ddg = urllib2.urlopen("https://api.duckduckgo.com/?q=" + string + "&format=json&pretty=1")
  return json.load(ddg)
  
