import urllib2
import json

def search(string):
  ddg = urllib2.urlopen("https://api.duckduckgo.com/?q=" + string + "&format=json&pretty=1")
  ddgapi = ddg.read()
  result = json.load(ddgapi)
  return result["RelatedTopics"][0]["Text"]
  
