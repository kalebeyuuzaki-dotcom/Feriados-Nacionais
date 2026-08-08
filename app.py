import requests
import time

from src.utils.funcoes import pegar_ano, formatar_data
from src.models.db import criar_db, inserir_feriado

criar_db()
lista_feriados = []

for ano in range(2114, 2115):
        url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
        response = requests.get(url)

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
        time.sleep(5)

inserir_feriado(lista_feriados)