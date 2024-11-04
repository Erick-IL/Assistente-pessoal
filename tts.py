import pyttsx3

class Call_TTS():
    def __init__(self):
        self.TTS = pyttsx3.init()
        voices = self.TTS.getProperty('voices')
        self.TTS.setProperty('voice', voices[1].id)

    def falar(self, text):
        self.TTS.say(text)
        self.TTS.runAndWait()

