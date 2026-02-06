from discord import Embed, Color
from api.youtubevideo import YouTubeVideo
import html

YOUTUBE_COLOR = Color.from_rgb(255, 0, 0)

def markdown_url(url: str, text: str = None) -> str:
    """Wraps URL to be clickable with with optional mask."""
    return f'[{text}]({url})' if text else f'<{url}>'


class BaseEmbed(Embed):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = Color.blurple()

class YouTubeVideoEmbed(BaseEmbed):
    def __init__(self, video: YouTubeVideo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title=html.unescape(video.title)
        self.description=markdown_url(video.video_link)
        self.color = YOUTUBE_COLOR
        self.set_thumbnail(url=video.video_thumbnail)
        self.add_field(
            name='Description',
            value=video.description,
            inline=False
        )