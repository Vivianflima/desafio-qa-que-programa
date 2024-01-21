def ordenar_lista():
    # Solicita ao usuário informar os números separados por vírgula
    entrada = input("Digite os números separados por vírgula e pressione enter. para decimais, utilize ponto: ")

    # Verifica se a entrada está vazia
    if not entrada:
        print("Array vazio. Nada a ordenar.")
        return

    # Converte a entrada para uma lista de números
    numeros = [float(num) for num in entrada.split(',')]

    # Ordena a lista
    numeros_ordenados = sorted(numeros)

    # Exibe o resultado sem casas decimais, se possível
    numeros_ordenados_int = [int(num) if num.is_integer() else num for num in numeros_ordenados]
    print("Lista Ordenada:", numeros_ordenados_int)

# Chamando a função principal
ordenar_lista()
