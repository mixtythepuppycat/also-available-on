import pytest
from api.track_service_util import get_tracks_from_message

# Integration tests with the music services

def test_simple_spotify_link():
    tracks = get_tracks_from_message("https://open.spotify.com/track/2Y0iGXY6m6immVb2ktbseM?si=7f2e8da2ffcc4d9f")
    assert len(tracks) == 3

def test_simple_ytmusic_link():
    tracks = get_tracks_from_message("https://music.youtube.com/watch?v=ETEg-SB01QY")
    assert len(tracks) == 3

def test_yt_link_does_not_response():
    tracks = get_tracks_from_message("https://www.youtube.com/watch?v=rtL5oMyBHPs")
    assert tracks is None

def test_track_inside_message():
    tracks = get_tracks_from_message("Checkout this track I found! https://open.spotify.com/track/2Y0iGXY6m6immVb2ktbseM?si=7f2e8da2ffcc4d9f It's really good!")
    assert len(tracks) == 3
    