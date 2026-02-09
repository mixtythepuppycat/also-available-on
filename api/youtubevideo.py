from json import loads as json_loads
from requests import get as requests_get
from keys import YOUTUBE_API_KEY
from logger import getLogger
from api.track_services import Track, TrackService
from api.track_service_names import ServiceNameEnum

_log = getLogger(__name__)

class YouTubeVideoTrack(Track):
    def __init__(self, payload: dict) -> None:
        item: dict = payload.get('items', [{}])[0]
        snippet: dict = item.get('snippet', {})
        self.video_id: str = item.get('id', {}).get('videoId')
        self.title: str = snippet.get('title')
        self.description: str = snippet.get('description')
        self.published_date: str = snippet.get('publishTime', '')[:10]

    def get_link(self) -> str:
        return f'https://www.youtube.com/watch?v={self.video_id}'

    def get_video_thumbnail(self) -> str:
        return f'https://i.ytimg.com/vi/{self.video_id}/default.jpg'
    
    def get_service_name(self) -> ServiceNameEnum:
        return ServiceNameEnum.YOUTUBE

class YouTubeVideoService(TrackService):
        
    def get_service_name(self) -> ServiceNameEnum:
        return ServiceNameEnum.YOUTUBE

    def search_for_track(self, query: str) -> Track:
        _log.info("Searching for " + query)

        yt_r = requests_get(
            'https://www.googleapis.com/youtube/v3/search'
            '?key={}'
            '&part=snippet'
            '&maxResults=1'
            '&type=video'
            '&q={}'.format(YOUTUBE_API_KEY, query)
        )
        content = json_loads(yt_r.content)

        if (error_code := yt_r.status_code) == 200:
            _log.info("Found")
            video = YouTubeVideoTrack(content)
        else:
            _log.error(content['error'][['message']])

        return video
    
    def get_name_and_artist_from_url(self, url: str) -> str:
        # TODO: implement
        return ""