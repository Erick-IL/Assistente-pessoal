# Ouvir e detectar palavra-chave → Usar SpeechRecognition ou Vosk.

import speech_recognition as sr

rec = sr.Recognizer() # inicialize recognizer

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic) # remove ambient noise
    while True:
        audio = rec.listen(mic, phrase_time_limit=1) # record audio 

        try:
            text = rec.recognize_google(audio, language="pt-BR")
            print(text)

            if 'olá' in text.lower():
                print('Olá para você também')
                break
            


        except sr.UnknownValueError:
                continue
        except sr.RequestError:
                print("Erro de comunicação com o serviço de reconhecimento.")
                break
