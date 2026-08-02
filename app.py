import requests
from src.utils.funcoes import pegar_ano

ano = pegar_ano()

# Url da api da página Brasil API
url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'

# Solicita os dados da página url
response = requests.get(url)

# Verifica o número do status HTTP da requisição da url
if response.status_code == 200:
    # Converte as informações da página para arquivo JSON
    dados_response = response.json