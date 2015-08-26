import urllib2
import json


def google_search(message):
    """
    Searches for a `search_term` which should be a string or a value that can be converted into a string.

    Parameters:
        - str `search_term`: a string to search for

    Returns a tuple (on success):
        - first value is a the first search results for the `search_term` returned by the Google API
        - second value is a Google Search UI URL, where more results can be obtained

    Returns False (on failure).

    """

    # The request also includes the userip parameter which provides the end
    # user's IP address. Doing so will help distinguish this legitimate
    # server-side traffic from traffic which doesn't come from an end-user.

    if len(message.split()) == 1:
        return ["No search term given", "message"]
    search_term = "+".join(message.split[1:]).encode('ascii', errors='replace')
    url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&userip=USERS-IP-ADDRESS" % search_term

    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)

    # Process the JSON string.
    results = json.load(response)

    # now have some fun with the results...
    if len(results["responseData"]["results"]) > 0:
        return [results["responseData"]["results"][0], results["responseData"]["cursor"]["moreResultsUrl"], "message"]

    return ["No results found for {}".format(search_term), "message"]
