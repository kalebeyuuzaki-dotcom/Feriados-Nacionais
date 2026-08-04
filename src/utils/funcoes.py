def pegar_ano():
    """Solicita ao usuário um número inteiro e positivo de exatamente 4 dígitos 
    e valida a entrada até que seja aceita. 
    """
    while True:
        # Pede a entrada como texto (string) primeiro
        entrada = input('Informe o ano: ').strip()
        # Verifica se possui 4 dígitos (Ex.: 2026) e se é somente números
        if not entrada.isdigit() or len(entrada) != 4:
            print('ERRO. Digite corretamente o ano. ')
            continue
        # Se passou na validação, converte e retorna
        ano = int(entrada)
        return ano

def formatar_data(data_str, separador: str = '-'):
    """Formata data do padrão 'AAAA-MM-DD' para o padrão 'DD/MM/AAAA'.
    Args:
        date_str (str): A string no formato original 'AAAA-MM-DD'.
        separador (str): Onde a data deve ser separada ('-', '/', ':')
    Returns:
        str: A data no formato 'DD/MM/AAAA'.
    """
    partes = data_str.split(f'{separador}')
    invertido = partes[::-1]
    return '/'.join(invertido)

# Área para testes
if __name__ == '__main__':
    data = '2026/08/04'
    data_ = formatar_data(data, '/')
    print(data_)