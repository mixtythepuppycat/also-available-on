from abc import ABC, abstractmethod
from api.track_service_names import ServiceNameEnum

class Track(ABC):
    @abstractmethod
    def get_link(self) -> str:
        pass

    @abstractmethod
    def get_service_name(self) -> ServiceNameEnum:
        pass

class TrackService(ABC):
    @abstractmethod
    def search_for_track(query: str) -> Track:
        pass

    @abstractmethod
    def get_name_and_artist_from_url(url: str) -> str:
        pass

    @abstractmethod
    def get_service_name(self) -> ServiceNameEnum:
        pass