  # artist info: user gives artist URI, get artist info
  # for future update: user gives artist name, get artist info
  # EXAMPLE USE: TAYLOR SWIFT URI: 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

import spotipy
from spotipy import util
from scripts.user_info import get_user
from scripts.prompts import prompt_user_artist_URI

def print_albums():
  albums = get_albums(get_user())
  for album in albums:
    print(album['name'])

def get_albums(sp):
  artist_uri = prompt_user_artist_URI()
  results = sp.artist_albums(artist_uri, album_type='album')
  albums = results['items']
  while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])
  return albums


if __name__ == "__main__":
  print_albums()

