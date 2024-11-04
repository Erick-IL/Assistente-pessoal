import recognition
import intepreter
import tts
# Executar comandos do sistema → Usar os, pyautogui, e subprocess.
# Falar respostas → Usar pyttsx3 ou gTTS.
# Memória limitada → Usar SQLite ou TinyDB.
rz = recognition.recognizer()
it = intepreter.Ia_Intepreter()
TTS = tts.Call_TTS()

# linha de excução
while True:
    # aguardar palavra chave e detetar
    rz.wait_key_word()
    # ativar deteção de voz e transcrever
    question = rz.wait_question()
    # mandar pra o intepreter
    reponse = it.response(question)
    # pegar o texto e usar o TTS -> TTs é uma merda os gratis pelo menos
    TTS.falar(reponse)



