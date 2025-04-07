import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, jsonify

