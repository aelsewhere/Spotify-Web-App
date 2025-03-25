import spotipy
from spotipy.oauth2 import SpotifyOAuth
from scripts.secret import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE


def auth_manage():
    return(SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))

def authenticate():
    auth_manager = auth_manage()
    try:
        spotify_client = spotipy.Spotify(auth_manager=auth_manager)
        return spotify_client
    except Exception as e:
        print(f"Error: {e}")
        return None

def auth_url():
    auth_manager = auth_manage()
    if auth_manager:
        return auth_manager.get_authorize_url()
    else:
        return None


if __name__ == '__main__':
    spotify_client = authenticate()
    if spotify_client:
        print("Authentication successful!")
    else:
        print("Authentication failed.")