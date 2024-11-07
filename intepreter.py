# Interpretar Perguntas ->
import google.generativeai as genai
from dotenv import load_dotenv
import os 

class Ia_Intepreter():
    def __init__(self):   
        load_dotenv()   
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel("gemini-1.5-pro")
        self.response_params = '\n(fale como se fosse uma conversação e não uma resposta em topicos, não use "sabe?", "tipo?" e sem inventar coisas me diga com as informações que você sabe)'

    def response(self, question) -> str:
        response = self.model.generate_content(
            question + self.response_params,
        )
        return response.text