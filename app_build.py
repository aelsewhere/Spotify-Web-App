from flask import Flask, render_template, jsonify, redirect, url_for, session, request
from scripts.auth import authenticate
from functools import wraps
import spotipy





# build 1
build_v1 = Flask(__name__)
build_v1.secret_key = 'kdjsfakjsdhfue9oweiuf8i'

# wrapper to check if user is authenticated
def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = session.get('access_token')
        if not access_token:
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function
def get_spotify_client():
    access_token = session.get('access_token')
    if not access_token:
        return None
    return spotipy.Spotify(auth=access_token)





@build_v1.route('/')
def home():
    return render_template('index.html')

@build_v1.route('/test-static')
def test_static():
    return build_v1.send_static_file('assets/css/styles.css')

@build_v1.route('/spotify-connect')
def spotify_connect():
    return render_template('spotconnect.html')

@build_v1.route('/spotify-login')
def spotify_login():
    from scripts.auth import auth_url
    auth_url = auth_url()
    if auth_url:
      return redirect(auth_url)
    else:
      return jsonify({'error': 'Spotify Login: authentication url not found.'})

@build_v1.route('/logout')
def logout():
    session.pop('access_token',None)
    return redirect(url_for('home'))

@ build_v1.route('/callback')
def callback():
    from flask import request
    from scripts.auth import auth_manage
    auth_manager = auth_manage()
    code = request.args.get('code')
    if not code:
        return jsonify({'error': 'Callback: authorization code not found.'})
    token_info = auth_manager.get_access_token(code)

    try:
       token_info = auth_manager.get_access_token(code)
       if token_info:
           session['access_token'] = token_info['access_token']
           return redirect(url_for('dashboard'))
       else:
           return jsonify({'error': 'Callback: token info not found.'})
    except Exception as e:
        return jsonify({'error': f'Callback: {e}'})





@ build_v1.route('/dashboard')
@ require_auth
def dashboard():
    sp = get_spotify_client()
    if not sp:
        return redirect(url_for('home'))
    try:
        # Fetch top 10 tracks
        top_tracks = sp.current_user_top_tracks(limit=10)
        tracks = [
            {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name']
            }
            for track in top_tracks['items']
        ]

        # Fetch recently played tracks
        recently_played = sp.current_user_recently_played(limit=10)
        recent_tracks = [
            {
                'name': item['track']['name'],
                'artist': item['track']['artists'][0]['name'],
                'album': item['track']['album']['name']
            }
            for item in recently_played['items']
        ]
    except Exception as e:
        tracks = []
        recent_tracks = []
        print(f"Error fetching data: {e}")
    return render_template('dashboard.html', tracks=tracks, recent_tracks=recent_tracks)

@build_v1.route('/about')
def about():
    return render_template('about.html')

@build_v1.route('/mood-select')
@build_v1.route('/mood-select.html')
def mood_select():
    return render_template('mood-select.html')

@build_v1.route('/mood-generate')
@build_v1.route('/mood-generate.html')
def mood_generate():
    moods = request.args.get('moods', '').split(',') if request.args.get('moods') else []
    return render_template('mood-generate.html', moods=moods)


@build_v1.route('/mood-generate/<moods>')
def mood_generate_with_moods(moods):
    moods = moods.split(',') if moods else []
    return render_template('mood-generate.html', moods=moods)

@build_v1.route('/media-select')
@build_v1.route('/media-select.html')
def media_select():
    return render_template('media-select.html')

@build_v1.route('/profile')
def profile():
    return render_template('profile.html')

@build_v1.route('/settings')
def settings():
    return render_template('settings.html')

@build_v1.route('/monthly-generate')
@require_auth
def monthly_generate():
    sp = get_spotify_client()
    if not sp:
        return redirect(url_for('home'))
    try:
        top_tracks = sp.current_user_top_tracks(limit=50)
        tracks = [
            {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name']
            }
            for track in top_tracks['items']
        ]
    except Exception as e:
        tracks = []
        recent_tracks = []
        print(f"Error fetching data: {e}")

    return render_template('monthly-generate.html', tracks=tracks)