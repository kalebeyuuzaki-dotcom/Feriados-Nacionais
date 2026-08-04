import requests
from src.utils.funcoes import pegar_ano, formatar_data

ano = pegar_ano()

# Url da api da página Brasil API
url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
# Solicita os dados da página url
response = requests.get(url)
# Verifica o número do status HTTP da requisição da url
if response.status_code == 200:
    dados_response = response.json()
    for feriado in dados_response:
        data_formatada = formatar_data(feriado['date'], "-")
        print(data_formatada, feriado['name'])