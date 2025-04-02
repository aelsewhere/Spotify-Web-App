import spotipy
from spotipy import util
from scripts.user_info import get_user

def get_audio_features(sp):
  track_uri = input("Enter the Spotify track URI: ")
  features = sp.audio_features(track_uri)
  return features