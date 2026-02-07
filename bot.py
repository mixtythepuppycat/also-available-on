import discord
import api.youtubevideo
import api.spotify
import api.youtubemusic 
from keys import BOT_TOKEN
from logger import getLogger
from embeds import YouTubeEmbed

_log = getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != "music":
        return

    if message.content.startswith('https://open.spotify.com/track/'):
        _log.info("Spotify URL found in chat: " + message.content)

        track = api.spotify.get_name_and_artist_from_url(message.content)
        ytvideo = api.youtubevideo.search_video(track)
        ytmusic = api.youtubemusic.search_youtube_music(track)

        await message.channel.send(embed=YouTubeEmbed(ytvideo, ytmusic))

    if message.content.startswith('https://music.youtube.com/watch?v='):
        _log.info("YouTube Music URL found in chat: " + message.content)
        
        track = api.youtubemusic.get_name_and_artist_from_url(message.content)
        result = api.spotify.search_spotify(track)

        await message.channel.send(result.music_link)


_log.info("STARTING BOT")
client.run(BOT_TOKEN)