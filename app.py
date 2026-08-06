import requests, time

from src.utils.funcoes import pegar_ano, formatar_data
from src.models.db import criar_db, inserir_feriado

ano = pegar_ano()
criar_db()
lista_feriados = []

# Url da api da página Brasil API
url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
# Solicita os dados da página url
response = requests.get(url)
# Verifica o número do status HTTP da requisição da url
if response.status_code == 200:
    dados_response = response.json()
    for feriado in dados_response:
        data_formatada = formatar_data(feriado['date'], "-")
        # Trata os dados para os adionar a lista de dicionário que irá para a função de inserir feriado ao database
        dados_tratados = {
            'date': data_formatada,
            'name': feriado['name']
        }

        lista_feriados.append(dados_tratados)

inserir_feriado(lista_feriados)



# '''O programa irá consumir a API da Brasil API para consultar feriados de 2026 até 2100 e guardar no banco de dados
# deve se iniciar com um for in range para cada {ano} na url, receber os dados em json e depois salvar no banco de dados.
# '''