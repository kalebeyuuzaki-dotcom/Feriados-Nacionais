import requests
import time

from src.utils.funcoes import pegar_ano, formatar_data
from src.models.db import criar_db, inserir_feriado, visualizar_tabela

criar_db()
lista_feriados = []

for ano in range(1900, 2027):
    try:
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

        elif response.status_code == 400:
            print("Erro. Ano não informado. ")

        elif response.status_code == 404:
            print("Erro. Ano fora do intervalo suportado. ")

        elif response.status_code == 500:
            print("Erro interno no serviço de feriados. ")

        time.sleep(1)
            
    except ValueError as e:
        print(f"Erro inesperado. {e}")

inserir_feriado(lista_feriados)