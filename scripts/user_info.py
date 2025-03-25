# description: get info about the user

import spotipy
from spotipy import util
from scripts.auth import authenticate

def user_info(top_tracks=10, top_artists=10, playlists=100):
  sp = get_user()
  get_user_display_name(sp)
  get_user_top_tracks(sp, top_tracks)
  get_user_top_artists(sp, top_artists)
  get_user_playlists(sp, playlists)

def get_user():
  sp = authenticate()
  return sp

def get_user_display_name(sp):
  user = sp.current_user()
  display_name = user['display_name']
  print(f"User: {display_name}")

def get_user_top_tracks(sp, top_tracks):
  tracks = sp.current_user_top_tracks(limit=top_tracks)
  print("Top tracks: ")
  for i, item in enumerate(tracks['items']):
    track = item['name']
    artist = item['artists'][0]['name']
    print(f"{i+1}. {track} by {artist}")

def get_user_top_artists(sp, top_artists):
  artists = sp.current_user_top_artists(limit=top_artists)
  print("Top artists: ")
  for i, item in enumerate(artists['items']):
    artist = item['name']
    print(f"{i+1}. {artist}")

def get_user_playlists(sp, playlists):
  playlists = sp.current_user_playlists(limit=playlists)
  print("Playlists: ")
  for i, item in enumerate(playlists['items']):
    playlist = item['name']
    print(f"{i+1}. {playlist}")

if __name__ == "__main__":
  user_info()
