import random
import string

def obter_comprimento():
    while True:
        try:
            comprimento = int(input("Digite em numéros o comprimento da senha desejada: "))
            if comprimento > 0:
                return comprimento
            else:
                print("Erro: O comprimento deve ser maior que zero.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

def obter_opcao(mensagem):
    while True:
        opcao = input(mensagem).lower()
        if opcao in ['s', 'n']:
            return opcao
        else:
            print("Erro: Resposta inválida. Digite 's' para Sim ou 'n' para Não.")

def gerar_senha(comprimento, incluir_numeros=True, incluir_maiusculas=True, incluir_minusculas=True, incluir_especiais=True):
    caracteres = ""
    
    if incluir_numeros:
        caracteres += string.digits
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro: Nenhum tipo de caractere selecionado.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    comprimento = obter_comprimento()
    incluir_numeros = obter_opcao("Incluir números? (s/n): ") == 's'
    incluir_maiusculas = obter_opcao("Incluir letras maiúsculas? (s/n): ") == 's'
    incluir_minusculas = obter_opcao("Incluir letras minúsculas? (s/n): ") == 's'
    incluir_especiais = obter_opcao("Incluir caracteres especiais? (s/n): ") == 's'

    senha = gerar_senha(comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais)

    if senha:
        print("Senha gerada:", senha)

if __name__ == "__main__":
    main()
