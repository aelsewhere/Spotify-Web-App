import spotipy
from spotipy import util

from scripts.user_info import get_user, get_user_playlists
from scripts.user_prompts import prompt_user_playlist_id



def playlist_info(sp):
  playlist_id = prompt_user_playlist_id()
  playlist = sp.playlist(playlist_id)
  print(f"Playlist: {playlist['name']}")
  print(f"Owner: {playlist['owner']['display_name']}")
  print(f"Description: {playlist['description']}")
  print(f"Number of tracks: {playlist['tracks']['total']}")
  
  

def print_playlists():
  playlists = get_user_playlists(get_user(), 10)

def print_songs(sp):
  playlist_id = prompt_user_playlist_id()
  playlist = sp.playlist(playlist_id)
  print("Tracks: ")
  for i, item in enumerate(playlist['tracks']['items']):
    track = item['track']['name']
    artist = item['track']['artists'][0]['name']
    print(f"{i+1}. {track} by {artist}")



if __name__ == "__main__":
  sp = get_user()
  print_songs(sp)