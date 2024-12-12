from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from funcions.recognition import recognizer
import spotipy
import os
import re

class SpotifyController:
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

    def search_info(self, info: dict, method: str, index: int = 0) -> dict:
        """Busca informações detalhadas sobre a música."""

        if method == 'single':
            return self._extract_single_music_info(info)
        elif method == 'multiple':
            return self._extract_multiple_music_info(info, index)

    def _extract_single_music_info(self, info: dict) -> dict:
        """Extrai informações da música (single)."""
        artists = [artist['name'] for artist in info['item']['album']['artists']]
        return {
            "artist": artists,
            "album_name": info['item']['album']["name"],
            "music_name": info['item']["name"],
            "release_date": info['item']['album']["release_date"],
            "id": info['item']['album']['id'],
            'link': info['item']['album']['external_urls']['spotify']
        }

    def _extract_multiple_music_info(self, info: dict, index: int) -> dict:
        """Extrai informações da música (multiple)."""
        artists = [artist['name'] for artist in info['tracks']['items'][index]['artists']]
        return {
            "artist": artists,
            "album_name": info['tracks']['items'][index]['album']["name"],
            "music_name": info['tracks']['items'][index]["name"],
            "release_date": info['tracks']['items'][index]['album']["release_date"],
            "id": info['tracks']['items'][index]['album']['id'],
            'link': info['tracks']['items'][index]['album']['external_urls']['spotify']
        }

    def toggle_playback(self, text: str):
        """Controla a reprodução da música (pausar, continuar, pular, voltar)."""
        if 'pausar' in text:
            self._pause_playback()
        elif 'continuar' in text or 'play' in text or 'retomar' in text:
            self._start_playback()
        elif 'passar' in text or 'proxima' in text or 'pular' in text:
            self._next_track()
        elif 'voltar' in text or 'retornar' in text:
            self._previous_track()

    def _pause_playback(self):
        try:
            self.sp.pause_playback()
        except Exception as e:
            self._handle_playback_error(e)

    def _start_playback(self):
        try:
            self.sp.start_playback()
        except Exception as e:
            self._handle_playback_error(e)

    def _next_track(self):
        try:
            self.sp.next_track()
        except Exception as e:
            self._handle_playback_error(e)

    def _previous_track(self):
        try:
            self.sp.previous_track()
        except Exception as e:
            self._handle_playback_error(e)

    def _handle_playback_error(self, error: Exception):
        """Tratamento de erro durante a reprodução."""
        if hasattr(error, 'http_status') and error.http_status == 403:
            print("Erro HTTP 403: Ação não permitida.")
        else:
            print(f"Erro durante a reprodução: {error}")

    def repeat(self, text: str):
        """Controla a repetição da música ou playlist."""
        if 'repetir musica' in text:
            self._set_repeat('track')
        elif 'repetir playlist' in text:
            self._set_repeat('context')
        elif 'desligar repetição' in text:
            self._set_repeat('off')
        elif 'aleatorio' in text:
            self._toggle_shuffle(True)
        elif 'reprodução normal' in text or 'desligar aleatorio' in text:
            self._toggle_shuffle(False)

    def _set_repeat(self, mode: str):
        try:
            self.sp.repeat(mode)
        except Exception as e:
            print(f"Erro ao definir repetição: {e}")

    def _toggle_shuffle(self, shuffle: bool):
        try:
            self.sp.shuffle(shuffle)
        except Exception as e:
            print(f"Erro ao definir shuffle: {e}")

    def get_info(self, text: str, music=None) -> dict:
        """Obtém informações sobre a música atual ou uma música especificada."""
        info = None
        if 'musica atual' in text or 'informação da musica atual' in text:
            info = self.search_info(self.sp.current_playback(), 'single')

        elif "info" in text:
            info = self.search_info(music, 'single')

        if info:
            requested_info = self._parse_requested_info(text, info)
            return requested_info

    def _parse_requested_info(self, text: str, info: dict) -> dict:
        """Analisa o texto e retorna as informações solicitadas sobre a música."""
        requested_info = {}
        verify_info = {
            "artist": "artista" in text or "cantor" in text,
            "date": "data" in text or "lançamento" in text,
            "album": "álbum" in text or "disco" in text,
            "name": "nome" in text or "título" in text
        }

        if not any(verify_info.values()):
            print(info)

        if verify_info["artist"]:
            requested_info["artist"] = info.get("artist")
        if verify_info["date"]:
            requested_info["date"] = info.get("release_date")
        if verify_info["name"]:
            requested_info["name"] = info.get("music_name")
        if verify_info["album"]:
            requested_info["album"] = info.get("album_name")

        return requested_info

    def search_music(self, text: str):
        """Busca músicas no Spotify com base na entrada do usuário."""
        if 'procurar' in text or 'buscar' in text:
            query = text.replace('procurar', '').replace('buscar', '').replace('musica', '')
            self._search_and_play(query)

    def _search_and_play(self, query: str): # analisar !
        """Realiza a busca da música e toca a primeira música encontrada."""
        search_results = self.sp.search(query, limit=3)
        for i in range(3):   
            music_info = self.search_info(search_results, 'multiple', index=i)
            print(music_info)
            print('Deseja tocar essa musica ou ver outra')
            text = recognizer.wait_question()
            if 'Tocar' in text:
                self.play_music(music_info['id'])
            if 'Passar' in text:
                pass

    def play_music(self, track_id: str): # incompleta
        """Toca a música especificada pelo ID da faixa."""
        self.sp.start_playback(uris=[f"spotify:track:{track_id}"])

    def volume(self, volume: int): # incompleta 
        """Ajusta o volume do Spotify."""
        self.sp.volume(volume)

    def treat_cmd(self, text: str):
        """Processa os comandos de controle de reprodução e busca de músicas."""
        text = text.lower()
        self.toggle_playback(text)
        self.repeat(text)
        self.get_info(text)
        self.search_music(text)


if __name__ == '__main__':
    controller = SpotifyController()
    controller.treat_cmd('')
    #a=  controller.sp.current_playback()
    #print(a)
