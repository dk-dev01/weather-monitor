import requests #chamada da api

chaveapi = '25bff31627fc1cd7a6763af378a1d194' #chave de acesso da api


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