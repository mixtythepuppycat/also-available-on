import discord
from api.youtubevideo import search_video
from api.spotify import get_name_and_artist_from_url
from api.youtubemusic import search_youtube_music
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

        track = get_name_and_artist_from_url(message.content)
        ytvideo = search_video(track)
        ytmusic = search_youtube_music(track)

        await message.channel.send(embed=YouTubeEmbed(ytvideo, ytmusic))

_log.info("STARTING BOT")
client.run(BOT_TOKEN)