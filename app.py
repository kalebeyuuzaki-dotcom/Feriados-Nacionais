import requests

from src.utils.funcoes import pegar_ano, formatar_data
from src.models.db import inserir_feriado

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



# '''O programa irá consumir a API da Brasil API para consultar feriados de 2026 até 2100 e guardar no banco de dados
# deve se iniciar com um for in range para cada {ano} na url, receber os dados em json e depois salvar no banco de dados.
# '''