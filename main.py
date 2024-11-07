import recognition
import intepreter
import tts
# Executar comandos do sistema → Usar os, pyautogui, e subprocess.

# Memória limitada → Usar SQLite ou TinyDB.
class virtual_assistant():
    def __init__(self):       
        self.rz = recognition.recognizer()
        self.it = intepreter.Ia_Intepreter()
        self.TTS = tts.Call_TTS()

    def inicializate(self):
        while True:
            self.rz.wait_key_word()





# while True:
#     # aguardar palavra chave e detetar
#     self.rz.wait_key_word()
#     # ativar deteção de voz e transcrever
#     question = self.rz.wait_question()
#     # mandar pra o intepreter
#     
#     # pegar o texto e usar o TTS -> TTs é uma merda os gratis pelo menos
#     self.TTS.falar(reponse)



