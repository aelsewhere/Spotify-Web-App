import spotipy
from spotipy import util
from scripts.user_info import get_user

def get_audio_features(sp):
  track_uri = prompt_user()
  features = sp.audio_features(track_uri)
  return features