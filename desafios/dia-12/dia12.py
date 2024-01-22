def analise_frequencia_letras(texto):
    # Inicializa um dicionário para armazenar a contagem de cada letra
    contagem_letras = {}

    # Itera sobre cada caractere no texto
    for caractere in texto:
        # Verifica se o caractere é uma letra
        if caractere.isalpha():
            # Converte o caractere para minúsculo para tratamento de maiúsculas/minúsculas
            letra = caractere.lower()

            # Atualiza a contagem no dicionário
            contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

    return contagem_letras

# Função para formatar e exibir o resultado da análise de frequência
def exibir_resultado(contagem_letras):
    print("Resultado:")
    for letra, contagem in contagem_letras.items():
        print(f"{letra}: {contagem}")

# Entrada do usuário
texto_usuario = input("Digite uma palavra ou frase para analisar a frequência de letras: ")  

# Realiza a análise de frequência
resultado_analise = analise_frequencia_letras(texto_usuario)

# Exibe o resultado
exibir_resultado(resultado_analise)
