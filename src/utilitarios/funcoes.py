# Solicita ao usuário um número inteiro e valida a entrada até que seja aceita
def pegar_ano():
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

# Área para testes
if __name__ == '__main__':
    vari = pegar_ano()
    print(f'O ano solicitado foi {vari}. ')