import urllib2
import json
# from bs4 import BeautifulSoup

def google_search(search_term):
    # send = {}
    # site = "http://www.google.com/search?tbm=isch&safe=strict&q=" + search_term
    # print site
    # hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}
    # req = urllib2.Request(site, headers=hdr)
    #
    # try:
    #     page = urllib2.urlopen(req)
    # except urllib2.HTTPError, e:
    #     print e.fp.read()
    #     return False
    #
    # search_page = page.read()
    # parsing_page = BeautifulSoup(search_page)
    # content = parsing_page.select("div.srg")[0]
    # tags = content.findAll("li", {"class": "g"}, limit=3)
    # result = []
    #
    # for i in tags:
    #     title = i.select(".r a")[0].decode_contents(formatter="html")
    #     link = i.select(".r a")[0].get("href")
    #     desc = i.select(".s div.st")[0].decode_contents(formatter="html")
    #     result.append({"title": title, "link": link, "description": desc})
    #
    #
    #
    # send["results"] = result
    # send["more"] = site
    # send["term"] = search_term
    #
    # return send

    # The request also includes the userip parameter which provides the end
    # user's IP address. Doing so will help distinguish this legitimate
    # server-side traffic from traffic which doesn't come from an end-user.
    url = ("https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + search_term + "&userip=USERS-IP-ADDRESS")

    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)

    # Process the JSON string.
    results = json.load(response)
    # now have some fun with the results...
    return results["responseData"]["results"][0]["content"]
