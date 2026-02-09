import spotipy
from api.track_services import Track, TrackService
from api.track_service_names import ServiceNameEnum
from keys import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from logger import getLogger
from spotipy.oauth2 import SpotifyClientCredentials

_log = getLogger(__name__)

class SpotifyTrack(Track):
    def __init__(self, payload: dict) -> None:
        item: dict = payload['tracks']['items'][0]
        self.video_id: str = item['id']

    def get_link(self) -> str:
        return f'https://open.spotify.com/track/{self.video_id}'
    
    def get_service_name(self) -> ServiceNameEnum:
        return ServiceNameEnum.SPOTIFY

class SpotifyService(TrackService):
    def __init__(self): 
        self._sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))
    
    def get_service_name(self) -> ServiceNameEnum:
        return ServiceNameEnum.SPOTIFY
    
    def search_for_track(self, query) -> Track:
        track = self._sp.search(query, limit=1, type='track')
        song = SpotifyTrack(track)

        return song

    def get_name_and_artist_from_url(self, url: str) -> str:
        _log.info("Searching for track: " + url)

        track = self._sp.track(url)
        track_formatted = track['name'] + ' ' + track['artists'][0]['name']

        _log.info("Found track: " + track_formatted)

        return track_formatted

  