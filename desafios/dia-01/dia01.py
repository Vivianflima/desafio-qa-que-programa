# Inserção de numero pelo usuário
try:
    numero = int(input("Digite um número: "))
#mensagem de erro caso o usuário insira qualquer caractere que não seja número
except ValueError:
    print("Erro: Por favor, insira apenas números.")
    exit()

# Verificação se o número é par ou ímpar
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")