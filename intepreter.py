# Interpretar Perguntas ->
import google.generativeai as genai
from dotenv import load_dotenv
import os
class Ia_Intepreter():
    def __init__(self):     
        load_dotenv()
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def response(self, question):
        response = self.model.generate_content(
            question + '(fale como se fosse uma conversação e não uma resposta em topicos)',
        )
        return response.text

