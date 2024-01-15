def contar_palavras(texto):
    # Remove espaços extras, divide o texto em palavras e retorna o número de palavras
    palavras = texto.split()
    return len(palavras)

# Solicita ao usuário inserir o texto
entrada = input("Digite o texto: ")

# Verifica o número de palavras
numero_palavras = contar_palavras(entrada)

# Exibe o resultado
print(f'O texto contém {numero_palavras} {"palavra" if numero_palavras == 1 else "palavras"}.')