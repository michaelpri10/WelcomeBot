import urllib2
from bs4 import BeautifulSoup
import random


def youtube_search(search_term):
    search_term = search_term.encode('ascii', errors='replace')
    youtube_page = urllib2.urlopen("https://www.youtube.com/results?search_query=" + search_term)
    parse_youtube = BeautifulSoup(youtube_page)
    video_parents = parse_youtube.select("ol.item-section > li > div.yt-lockup > div.yt-lockup-dismissable > div.yt-lockup-content > h3.yt-lockup-title > a")
    video_links = ["https://www.youtube.com" + i['href'] for i in video_parents]
    if len(video_links) == 0:
        return False
    else:
        return random.choice(video_links)
