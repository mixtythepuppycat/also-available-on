from ytmusicapi import YTMusic
from logger import getLogger
from urllib.parse import urlparse
from urllib.parse import parse_qs
from api.track_services import Track, TrackService
from api.track_service_names import ServiceNameEnum

_log = getLogger(__name__)

class YouTubeMusicTrack(Track):
    def __init__(self, payload: dict = None, url: str = None) -> None:
        if payload is not None:
            item: dict = payload[0]
            self.video_id: str = item['videoId']
            self.link_format = f'https://music.youtube.com/watch?v={self.video_id}'
        if url is not None:
            self.link_format: str = url

    def get_link(self) -> str:
        return self.link_format
    
    def get_service_name(self) -> ServiceNameEnum:
        return ServiceNameEnum.YOUTUBE_MUSIC 

class YouTubeMusicService(TrackService):
    def __init__(self): 
        self._ytmusic = YTMusic()

    def get_service_name(self) -> ServiceNameEnum:
        return ServiceNameEnum.YOUTUBE_MUSIC

    def search_for_track(self, query: str) -> Track:
        content = self._ytmusic.search(query)

        if content.count == 0:
            _log.error("Could find a song with query: " + query)
            return 
        else:
            video = YouTubeMusicTrack(content)
            return video
        
    def get_name_and_artist_from_url(self, url: str) -> str:
        parsed_url = urlparse(url)
        videoId = parse_qs(parsed_url.query)['v'][0]

        content = self._ytmusic.get_song(videoId)

        return content['videoDetails']['author'] + " " + content['videoDetails']['title']
    
    def get_track_from_url(self, url: str) -> Track:
        return YouTubeMusicTrack(url=url)
