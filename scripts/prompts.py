import spotipy
from spotipy import util


def prompt_user_artist_URI():  
  artist_uri = input("Enter the artist URI: ")
  if not artist_uri:
    artist_uri = input("Enter the artist URI: ")
  return artist_uri

def prompt_user_playlist_id():
  playlist_id = input("Enter the playlist ID: ")
  if not playlist_id:
    playlist_id = input("Enter the playlist ID: ")
  return playlist_id