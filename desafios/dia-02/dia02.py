# Solicita ao usuário inserir o primeiro número
num1 = input("Digite o primeiro número: ")

# Informa ao usuário sobre o uso de ponto para decimais
print("Lembre-se: Para números decimais, utilize ponto (.) ao invés de vírgula (,).")

# Solicita ao usuário escolher a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Verifica se a operação é válida
if operacao not in ['+', '-', '*', '/']:
    print("Erro: Operação inválida. Comece novamente")
    exit()

# Solicita ao usuário inserir o segundo número
num2 = input("Digite o segundo número: ")

# Tenta converter os números de String para float
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Erro: Caractere inválido inserido. Certifique-se de usar apenas números ou utilizar ponto '.' em caso de número decimal. Comece novamente")
    exit()

# Realiza a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    # Verifica se o segundo número é zero antes de realizar a divisão
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Não é possível dividir por zero.")
        exit()

# Exibe o resultado
print(f"Resultado: {resultado}")
