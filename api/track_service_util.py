from api.spotify import SpotifyService
from api.track_service_names import ServiceNameEnum
from api.track_services import Track, TrackService
from api.youtubemusic import YouTubeMusicService
from api.youtubevideo import YouTubeVideoService

allMusicServices: list[TrackService] = [YouTubeMusicService, SpotifyService, YouTubeVideoService]

def get_tracks_from_url(url: str, serviceName: ServiceNameEnum)  -> tuple[str, list[Track]]:
    serviceInstances: list[TrackService] = []
    trackList: list[Track] = []

    for service in allMusicServices:
        instance = service()

        if instance.get_service_name() is serviceName:
            query = instance.get_name_and_artist_from_url(url)
            trackList.append(instance.get_track_from_url(url))
        else:
            serviceInstances.append(service())

    for instance in serviceInstances:
        trackList.append(instance.search_for_track(query))
    
    return query, trackList