import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Get Spotify credentials from environment variables
import os
SPOTIPY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('REDIRECT_URI')
SPOTIPY_SCOPE = 'SCOPE'

# Authenticate with auth.py
from scripts.auth import authenticate
spotify_client = authenticate()

# Get User Info
from scripts.user_info import get_user_top_tracks_uri





def generate_top_50_songs():
    # Get the user's top tracks
    top_tracks = get_user_top_tracks_uri(spotify_client, top_tracks=50)
    # Get 



if __name__ == "__main__":
    generate_top_50_songs()

