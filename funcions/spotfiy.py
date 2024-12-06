from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import spotipy
import os 

# Substitua com suas próprias credenciais do Spotify Developer
class spotify():
    def __init__(self):       
        load_dotenv()
        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = "http://localhost:8888/callback"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=self.client_id, 
        client_secret=self.client_secret,
        redirect_uri=self.redirect_uri,
        scope="user-read-playback-state user-modify-playback-state"
        ))
        
    def current_music(self) -> str:
        '''
        Return essential info about current music 
        '''
        artists = []
        info = self.sp.current_playback()
        for artist in info['item']["artists"]: artists.append(artist['name'])
        music_name = info['item']["name"]
        album_name = info['item']['album']["name"]
        release_date = info['item']['album']["release_date"]
        status = info['is_playing']

        return artists, music_name, album_name, release_date, status
        
    def toggle_playback(self, text):
        '''
        toggle or return/pass the current music 
        '''
        if text == 'pausar':
            try:
                self.sp.pause_playback()
            except Exception as e:
                if e.http_status == 403:
                    self.sp.start_playback()
                else:
                   print(f"Erro HTTP: {e.http_status} - {e.msg}")
        elif text in ['continue', 'play', 'retomar']:
            try:
                self.sp.start_playback()
            except Exception as e:
                if e.http_status == 403:
                    print("A musica já está tocando")
                else:
                    print(f"Erro HTTP: {e.http_status} - {e.msg}")
        elif text in ['Passar', 'proxima', 'pular']:
            try:
                self.sp.next_track()
            except Exception as e:
                print(f"Erro HTTP: {e.http_status} - {e.msg}")
        elif text in ['voltar', 'retornar']:
            try:
                self.sp.previous_track()
            except Exception as e:
                print(f"Erro HTTP: {e.http_status} - {e.msg}")
    
    def play_music(self):
        ...
    
    def get_info(self):
        ...

    def search_music(self):
        ...
    

    

            
        
    
    
        


if __name__ == '__main__':
    control_player = spotify()
    control_player.toggle_playback("voltar")










            # if text == 'tocar':
            
            # track_uri = "spotify:track:6LANMfXqjzi25G6YTUrIFz"
            # # https://open.spotify.com/intl-pt/track/'45fJJLdP2qJ05S03FDwS6V'?si=b081a90597e841cc

            # # Iniciar a reprodução no dispositivo ativo
            # self.sp.start_playback(uris=[track_uri]