import re

def remove_caracteres_especiais(frase):
    # Remove espaços em branco, pontuação e converte para minúsculas
    return re.sub(r'[^a-zA-Z0-9]', '', frase).lower()

def eh_palindromo(frase):
    frase_processada = remove_caracteres_especiais(frase)
    inverso = frase_processada[::-1]
    return frase_processada == inverso

# Solicita ao usuário inserir a palavra ou frase
entrada = input("Digite a palavra ou frase: ")

# Verifica se é um palíndromo
if eh_palindromo(entrada):
    print(f'A entrada "{entrada}" é um palíndromo!')
else:
    print(f'A entrada "{entrada}" não é um palíndromo.')