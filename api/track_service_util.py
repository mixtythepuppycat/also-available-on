from api.spotify import SpotifyService
from api.track_service_names import ServiceNameEnum
from api.track_services import Track, TrackService
from api.youtubemusic import YouTubeMusicService
from api.youtubevideo import YouTubeVideoService
import re
from logger import getLogger

_log = getLogger(__name__)

allMusicServices: list[TrackService] = [YouTubeMusicService, SpotifyService, YouTubeVideoService]

def get_tracks_from_url(url: str, serviceName: ServiceNameEnum) -> list[Track]:
    serviceInstances: list[TrackService] = []
    trackList: list[Track] = []

    for service in allMusicServices:
        if service.get_service_name() is serviceName:
            instance = service()

            query = instance.get_name_and_artist_from_url(url)
            trackList.append(instance.get_track_from_url(url))
        else:
            serviceInstances.append(service())

    for instance in serviceInstances:
        trackList.append(instance.search_for_track(query))
    
    return trackList

def get_tracks_from_message(message: str):
    urls = re.findall(r'(https?://\S+)', message)

    # Just grab the first match since the main use case is just for single links
    match = next(((service, url) 
                  for service in allMusicServices 
                  for url in urls 
                  if url.startswith(service.get_url_starts_with())
                  ), None)

    if match:
        service, url = match

        _log.info(f"{service.get_service_name().value} URL found: {url}")

        return get_tracks_from_url(url, service.get_service_name())

    return None