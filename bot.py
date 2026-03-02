import discord
from api.track_service_names import ServiceNameEnum
from api.track_service_util import get_tracks_from_message
from keys import BOT_TOKEN, CHANNEL_NAME
from logger import getLogger
from embeds import TracksEmbed

_log = getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != CHANNEL_NAME:
        return

    try:
        tracks = get_tracks_from_message(message.content)

        if tracks:
            discordEmbed = TracksEmbed(tracks)
            await message.channel.send(embed=discordEmbed)
    except:
        _log.exception("Error during link processing")
        await message.reply("Sorry! I saw your link but something went wrong on my end.")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

_log.info("STARTING BOT")
client.run(BOT_TOKEN)