# Ouvir e detectar palavra-chave → Usar SpeechRecognition ou Vosk.

import speech_recognition as sr

rec = sr.Recognizer() # inicialize recognizer

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic) # remove ambient noise
    audio = rec.listen(mic) # record audio 
    try:
        text = rec.recognize_google(audio, language="pt-BR") # rocognize words in audio
        print(text)
    except:
        print('Desculpe, não consegui escutar')
