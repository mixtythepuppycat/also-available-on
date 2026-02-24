# Also Available On
A Discord bot that replies to music links with an embed containing links for that track on other services.

## Watched Link Types
- https://open.spotify.com/track/
- https://music.youtube.com/watch

## Supported Music Services In The Response
- YouTube
- YouTube Music
- Spotify 

## Hosted Instance
If you want to add the bot to your Discord server:
[click here](https://discord.com/oauth2/authorize?client_id=1469402290979999839&permissions=2048&integration_type=0&scope=bot). This instance only looks for links in the #music channel of your Discord.

## Self Host
If you want to host your own instance of the bot, it's strongly suggested that you use docker. To build the container use `docker build .` or use `docker-compose build`. You'll need to setup an `.env` file with your API keys from the following services:
- [Discord](https://discord.com/developers/applications)
- [Spotify](https://developer.spotify.com/)
- [Google Cloud](https://console.cloud.google.com/apis) with the YouTube Data API v3 enabled

See `keys.py` for more details