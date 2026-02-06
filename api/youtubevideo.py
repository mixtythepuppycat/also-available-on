from json import loads as json_loads
from requests import get as requests_get
from keys import YOUTUBE_API_KEY
from logger import getLogger

_log = getLogger(__name__)

class YouTubeVideo:
    def __init__(self, payload: dict) -> None:
        item: dict = payload.get('items', [{}])[0]
        snippet: dict = item.get('snippet', {})
        self.video_id: str = item.get('id', {}).get('videoId')
        self.title: str = snippet.get('title')
        self.description: str = snippet.get('description')
        self.published_date: str = snippet.get('publishTime', '')[:10]

    @property
    def video_link(self) -> str:
        return f'https://www.youtube.com/watch?v={self.video_id}'

    @property
    def video_thumbnail(self) -> str:
        return f'https://i.ytimg.com/vi/{self.video_id}/default.jpg'


def search_video(query: str) -> YouTubeVideo:
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
        video = YouTubeVideo(content)
    else:
        _log.error(content['error'][['message']])

    return video