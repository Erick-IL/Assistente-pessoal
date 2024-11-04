# Interpretar Perguntas ->
import google.generativeai as genai

class Ia_Intepreter():
    def __init__(self):      
        genai.configure(api_key="AIzaSyC9bsa8KqT2Y7rv9L93VmT48TghLWlUQTY")
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def response(self, question):
        response = self.model.generate_content(
            question + '(fale como se fosse uma conversação e não uma resposta em topicos,  não use "sabe?", "tipo? e sem inventar coisas me diga com as informações que você sabe")',
        )
        return response.text

