import requests #chamada da api
import os #para pegar a chave da api do arquivo .env
from dotenv import load_dotenv

load_dotenv()  #carrega as variaveis de ambiente do arquivo .env
chaveapi = os.getenv('chave')  #chave de acesso da api


def buscarClima(cidade):

    link = (f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chaveapi}&units=metric&lang=pt_br')

    resposta = requests.get(link)

    dados = resposta.json()

    if resposta.status_code != 200:
        return None

    temperatura = dados['main']['temp']
    temp_max = dados['main']['temp_max']
    temp_min = dados['main']['temp_min']
    umidade = dados['main']['humidity']
    vento = dados['wind']['speed']

    cidade_nome = dados['name']

    return {
        'cidade': cidade_nome,
        'temperatura': temperatura,
        'temp_max': temp_max,
        'temp_min': temp_min,
        'umidade': umidade,
        'vento': vento
    }