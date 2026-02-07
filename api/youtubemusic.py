from ytmusicapi import YTMusic
from logger import getLogger
from urllib.parse import urlparse
from urllib.parse import parse_qs

_log = getLogger(__name__)

class YouTubeMusic:
    def __init__(self, payload: dict) -> None:
        item: dict = payload[0]
        self.video_id: str = item['videoId']

    @property
    def music_link(self) -> str:
        return f'https://music.youtube.com/watch?v={self.video_id}'

ytmusic = YTMusic()

def search_youtube_music(query):
    ytmusic = YTMusic()

    content = ytmusic.search(query)

    if content.count == 0:
        _log.error("Could find a song with query: " + query)
        return 
    else:
        video = YouTubeMusic(content)
        return video
    
def get_name_and_artist_from_url(url):
    ytmusic = YTMusic()

    parsed_url = urlparse(url)
    videoId = parse_qs(parsed_url.query)['v'][0]

    content = ytmusic.get_song(videoId)

    return content['videoDetails']['author'] + " " + content['videoDetails']['title']
