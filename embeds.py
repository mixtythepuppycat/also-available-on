from discord import Embed, Color
from api.track_services import ServiceNameEnum, Track
import html

YOUTUBE_COLOR = Color.from_rgb(255, 0, 0)

def markdown_url(url: str, text: str = None) -> str:
    """Wraps URL to be clickable with with optional mask."""
    return f'[{text}]({url})' if text else f'<{url}>'


class BaseEmbed(Embed):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = Color.blurple()

class TracksEmbed(BaseEmbed):
    def __init__(self, tracks: list[Track], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for track in tracks:
            if track.get_service_name() is ServiceNameEnum.YOUTUBE:
                self.title=html.unescape(track.title)
                self.color = YOUTUBE_COLOR
                self.set_thumbnail(url=track.get_video_thumbnail())

                self.add_field(
                    name='YouTube',
                    value=track.get_link(),
                    inline=False
                )

                # add description as last field
                description = track.description,
            else:
                self.add_field(
                    name=track.get_service_name().value,
                    value=track.get_link(),
                    inline=False
                )

        self.add_field(
            name='Description',
            value=description,
            inline=False
        )