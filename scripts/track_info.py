import spotipy

def get_track_names(sp, track_uris):
    tracks = sp.tracks(track_uris)
    track_names = [track['name'] for track in tracks['tracks']]
    return track_names

def get_albums(sp, track_uris):
    tracks = sp.tracks(track_uris)
    albums = [track['album']['name'] for track in tracks['tracks']]
    return albums

def get_album_covers(sp, track_uris):
    tracks = sp.tracks(track_uris)
    album_covers = [track['album']['images'][0]['url'] for track in tracks['tracks']]
    return album_covers