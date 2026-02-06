import spotipy
from keys import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from logger import getLogger

_log = getLogger(__name__)

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))

def get_name_and_artist_from_url(url):
    _log.info("Searching for track: " + url)

    track = sp.track(url)
    track_formatted = '{} {}'.format(track['name'], ' '.join(track['artists'][0]['name']))

    _log.info("Found track: " + track_formatted)

    return track_formatted