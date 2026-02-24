from os import getenv

# Discord bot token
BOT_TOKEN: str = getenv('BOT_TOKEN')

# Spotify API client ID
SPOTIFY_CLIENT_ID: str = getenv('SPOTIFY_CLIENT_ID')

# Spotify API client secret
SPOTIFY_CLIENT_SECRET: str = getenv('SPOTIFY_CLIENT_SECRET')

# Google API key
YOUTUBE_API_KEY: str = getenv('YOUTUBE_API_KEY')

# Discord channel to watch for links
CHANNEL_NAME: str = getenv('CHANNEL_NAME', "music")