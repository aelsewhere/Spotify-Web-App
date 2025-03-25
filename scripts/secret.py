import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', "http://127.0.0.1:5000/callback")
SCOPE = 'user-library-read user-top-read user-read-recently-played user-read-playback-state user-modify-playback-state user-read-currently-playing'