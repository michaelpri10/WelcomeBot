import urllib2
import json


def google_search(search_term):

    # The request also includes the userip parameter which provides the end
    # user's IP address. Doing so will help distinguish this legitimate
    # server-side traffic from traffic which doesn't come from an end-user.
    url = ("https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + search_term + "&userip=USERS-IP-ADDRESS")

    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)

    # Process the JSON string.
    results = json.load(response)
    # now have some fun with the results...
    if len(results["responseData"]["results"]) > 1:
        return False
    else:
        return results["responseData"]["results"][0]["content"]
