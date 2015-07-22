import urllib2
import json

def search(string):
  ddg = urllib2.urlopen("https://api.duckduckgo.com/?q=" + string.replace(" ","+") + "&format=json&pretty=1")
  result = {}
  result["results"] = json.load(ddg)
  result["term"] = "https://api.duckduckgo.com/?q=" + string.replace(" ","+") + "&format=json&pretty=1"
  
  return result
  
