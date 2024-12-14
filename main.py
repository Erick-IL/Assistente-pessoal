import Assistente.core.recognition as recognition
import Assistente.core.intepreter as intepreter
from Assistente.features.spotfiy import SpotifyController 
import Assistente.core.tts as tts
# Executar comandos do sistema → Usar os, pyautogui, e subprocess.
class virtual_assistant():
    def __init__(self):       
        self.rz = recognition.recognizer()
        self.it = intepreter.Ia_Intepreter()
        self.TTS = tts.Call_TTS()
        self.sp = SpotifyController()

    def inicializate(self):
        while True:
            question = self.rz.wait_key_word()
            self.sp.treat_cmd(question)

if __name__ == '__main__':
    va = virtual_assistant()
    va.inicializate()