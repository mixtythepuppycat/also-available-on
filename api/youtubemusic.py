from ytmusicapi import YTMusic
from logger import getLogger

_log = getLogger(__name__)

ytmusic = YTMusic()

def search_youtube_music(query):
    ytmusic = YTMusic()

    content = ytmusic.search(query)

    if content.count == 0:
        _log.error("Could find a song with query: " + query)
        return 
    else:
        return "https://music.youtube.com/watch?" + content[0]['videoId']
