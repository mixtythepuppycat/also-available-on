import discord
from api.track_service_names import ServiceNameEnum
from api.track_service_util import get_tracks_from_url
from keys import BOT_TOKEN, CHANNEL_NAME
from logger import getLogger
from embeds import TracksEmbed

_log = getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != CHANNEL_NAME:
        return

    if message.content.startswith('https://open.spotify.com/track/'):
        _log.info("Spotify URL found in chat: " + message.content)

        try:
            query, tracks = get_tracks_from_url(message.content, ServiceNameEnum.SPOTIFY)
            discordEmbed = TracksEmbed(tracks)

            await message.channel.send(embed=discordEmbed)
        except:
            _log.exception("Error during Spotify link")
            await message.reply("Sorry! I saw your Spotify link but something went wrong on my end.")

    if message.content.startswith('https://music.youtube.com/watch?v='):
        _log.info("YouTube Music URL found in chat: " + message.content)
        
        try:
            query, tracks = get_tracks_from_url(message.content, ServiceNameEnum.YOUTUBE_MUSIC)
            discordEmbed = TracksEmbed(tracks)

            await message.channel.send(embed=discordEmbed)
        except:
            _log.exception("Error during YouTube Music link")
            await message.reply("Sorry! I saw your YouTube Music link but something went wrong on my end.")

_log.info("STARTING BOT")
client.run(BOT_TOKEN)