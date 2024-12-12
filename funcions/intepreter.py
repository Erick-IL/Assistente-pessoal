# Interpretar Perguntas ->
import google.generativeai as genai
from dotenv import load_dotenv
import os

class Ia_Intepreter():
    def __init__(self):     
        load_dotenv()
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.response_params = '\n(fale como se fosse uma conversação e não uma resposta em topicos, não use "sabe?", "tipo?" e sem inventar coisas me diga com as informações que você sabe)'

    def response(self, question) -> str:
        response = self.model.generate_content(
            question + self.response_params,
        )
        return response.text
    
    def treat_command(self, question) -> str:
        response = self.model.generate_content(
            question + '(pegue essas essa frase e pegue as informações importantes, tire os acentos e separe com apenas espaços, as palavras chaves são (tocar|reproduzir|pausar|continue|play|retomar|passar|proxima|pular|voltar|retornar|repetir musica|repetir playlist|desligar repetição|aleatorio|reprodução normal|desligar aleatorio|info|artista|cantor|data|lançamento|álbum|disco|nome|título|Tocar|procurar proxima|procurar outra|outra|procurar|buscar|informação|informações|musica atual|da musica atual))',
        )
        return response.text
    
if __name__ == '__main__':
    ia = Ia_Intepreter()
    print(ia.treat_command('informação da musica atual'))
    
