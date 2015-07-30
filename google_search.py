import urllib2
import json


def google_search(search_term):
    """
    Searches for a `search_term` which should be a string or a value convertable to string.

    Parameters:
        - str `search_term`: a string to search for

    Returns a tuple (on success):
        - first value is a list of search results for the `search_term` returned by Google API
        - second value is a Google Search UI URL, where more results can be obtained

    Returns False (on failure).

    --
    Authors:
        - michaelpri10
        - Jacob-Gray
        - Kubo2
    """

    # The request also includes the userip parameter which provides the end
    # user's IP address. Doing so will help distinguish this legitimate
    # server-side traffic from traffic which doesn't come from an end-user.
    url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&userip=USERS-IP-ADDRESS" % search_term

    request = urllib2.Request(url, None)
    response = urllib2.urlopen(request)

    # Process the JSON string.
    results = json.load(response)

    # now have some fun with the results...
    if len(results["responseData"]["results"]) > 0:
        return results["responseData"]["results"], results["responseData"]["cursor"]["moreResultsUrl"]

    return False
