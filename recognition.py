import speech_recognition as sr
# Ouvir e detectar palavra-chave → Usar SpeechRecognition.

class recognizer():
     def __init__(self):
          self.rec = sr.Recognizer()
        
     def wait_key_word(self):
        with sr.Microphone() as mic:
            self.rec.adjust_for_ambient_noise(mic) # remove ambient noise
            while True:
                audio = self.rec.listen(mic) # record audio
                try:
                    text = self.rec.recognize_google(audio, language="pt-BR")
                    print(text)

                    if 'roger' in text.lower():
                        print('Olá para você também')
                        break
                    
                except sr.UnknownValueError:
                        continue
                except sr.RequestError:
                        print("Erro de comunicação com o serviço de reconhecimento.")
                        break   
                
     def wait_question(self):
        with sr.Microphone() as mic: 
                 self.rec.adjust_for_ambient_noise(mic)
                 audio = self.rec.listen(mic)
                 try:
                    text = self.rec.recognize_google(audio, language="pt-BR")
                    print(text)
                    return text
                 except:
                      return 'Desculpe, não entendi'


