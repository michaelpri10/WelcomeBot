import urllib2
import json

def search(string):
  send = {}
  site = "http://www.google.com/search?tbm=isch&safe=strict&q=" + search_term
  print site
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}
  req = urllib2.Request(site, headers=hdr)

  try:
      page = urllib2.urlopen(req)
  except urllib2.HTTPError, e:
      print e.fp.read()
      return False

  google = page.read()
  parsing_page = BeautifulSoup(google)
  content = google.select("div.srg")[0]
  tags = content.findAll("li", {"class": "g"}, limit=3)
  result = []
  
  for el in tags:
    title = el.select(".r a")[0].decode_contents(formatter="html")
    link = el.select(".r a")[0].get("href")
    desc = el.select(".s div.st")[0].decode_contents(formatter="html")
    result.append({"title":title,"link":link,"description":desc})
    
    
  
  send["results"] = result
  send["more"] = site
  send["term"] = string
  
  return send
  
