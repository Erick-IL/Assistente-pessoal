import speech_recognition as sr
from funcions.intepreter import Ia_Intepreter
from funcions.tts import Call_TTS
# Ouvir e detectar palavra-chave → Usar SpeechRecognition.

class recognizer():
     def __init__(self):
          self.rec = sr.Recognizer()
          self.it = Ia_Intepreter()
          self.TTS = Call_TTS()       
             
     def wait_question(self) -> str:
        ''' wait user input '''
        with sr.Microphone() as mic: 
                 self.rec.adjust_for_ambient_noise(mic)
                 audio = self.rec.listen(mic)
                 try:
                    text = self.rec.recognize_google(audio, language="pt-BR")
                    print(text)
                    return text
                 except:
                      return 'Desculpe, não entendi'

     def wait_key_word(self) -> str:
        ''' wait for a key word and return a question/str '''
        with sr.Microphone() as mic:
            self.rec.adjust_for_ambient_noise(mic) # remove ambient noise
            while True:
                audio = self.rec.listen(mic) # record audio
                try:
                    text = self.rec.recognize_google(audio, language="pt-BR")
                    print(text) # rev

                    if 'roger' in text.lower():
                        self.TTS.speak('Olá! Como posso ajudar você hoje?')
                        question = self.wait_question()
                        return question
                  
                except sr.UnknownValueError:
                        continue
                except sr.RequestError:
                        print("Erro de comunicação")
                        break   

