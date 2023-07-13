import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    client_id = os.environ.get('client_id')  # Update with your actual client ID
    client_secret = os.environ.get('client_secret')  # Update with your actual client secret
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    spotify_data = sp.playlist_tracks(playlist_URI)   
    
    s3_client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    s3_client.put_object(
        Bucket="spotify-etl",  # Update with your actual S3 bucket name
        Key="raw_data/to_process/" + filename,  # Update the key/path where you want to store the file
        Body=json.dumps(spotify_data)
    )
