def converter_quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

def converter_milhas_para_quilometros(milhas):
    return milhas * 1.60934

def converter_metros_para_pes(metros):
    return metros * 3.28084

def converter_pes_para_metros(pes):
    return pes * 0.3048

def converter_celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def converter_fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para receber entrada do usuário e mostrar o resultado
def converter_unidades():
    # Solicita ao usuário a unidade de medida a ser convertida
    unidade_origem = input("Digite a unidade de medida a ser convertida (Quilômetros (km), Milhas (mi), Metros (m), Pés (ft), Celsius (C), Fahrenheit (F)): ").lower()

    # Solicita ao usuário o valor a ser convertido
    valor = float(input(f"Digite o valor em {unidade_origem}: "))

    # Realiza a conversão com base na unidade de medida escolhida
    if unidade_origem == "km":
        resultado = converter_quilometros_para_milhas(valor)
        unidade_destino = "milhas (mi)"
    elif unidade_origem == "mi":
        resultado = converter_milhas_para_quilometros(valor)
        unidade_destino = "Quilômetros (km)"
    elif unidade_origem == "m":
        resultado = converter_metros_para_pes(valor)
        unidade_destino = "Pés (ft)"
    elif unidade_origem == "ft":
        resultado = converter_pes_para_metros(valor)
        unidade_destino = "Metros (m)"
    elif unidade_origem == "c":
        resultado = converter_celsius_para_fahrenheit(valor)
        unidade_destino = "Fahrenheit (F)"
    elif unidade_origem == "f":
        resultado = converter_fahrenheit_para_celsius(valor)
        unidade_destino = "Celsius (C)"
    else:
        print("Unidade de medida não reconhecida. Verifique a digitação e tente novamente.")
        return

    # Exibe o resultado da conversão
    print(f"Resultado da conversão: {resultado} {unidade_destino}")

# Chamando a função principal
converter_unidades()


