import random

# Variáveis globais
pontuacao = 0
limite_tentativas = 7

# Função para gerar um novo número aleatório
def gerar_numero():
    return random.randint(1, 100)

# Função para mostrar o menu inicial
def mostrar_menu():
    print("===== Jogo da Adivinhação =====")
    print("1. Jogar")
    print("2. Ver Pontuação")
    print("3. Zerar Pontuação")
    print("4. Sair")

# Função principal
def jogar_adivinhacao():
    global pontuacao
    global limite_tentativas

    while True:
        mostrar_menu()
        opcao = input("Jogo de adivinhação da Vivi!Escolha uma opção (1-4): ")

        if opcao == "1":
            pontuacao += jogar_rodada()
        elif opcao == "2":
            print(f"Sua pontuação atual no jogo de adivinhação da Vivi: {pontuacao} ponto(s)")
        elif opcao == "3":
            pontuacao = 0
            print("Pontuação zerada.")
        elif opcao == "4":
            print("Obrigado por jogar o jogo de adivinhação da Vivi. Até a próxima!")
            break
        else:
            print("Opção incorreta! Digite '1' para Jogar, '2' para Ver Pontuação, '3' para Zerar Pontuação ou '4' para Sair.")

# Função para uma rodada do jogo
def jogar_rodada():
    global limite_tentativas
    numero_correto = gerar_numero()

    print("Jogo de adivinhação da Vivi! Tente adivinhar o número entre 1 e 100!")

    for tentativa_atual in range(1, limite_tentativas + 1):
        tentativa = int(input(f"Tentativa {tentativa_atual}: "))
        
        if tentativa == numero_correto:
            print(f"Parabéns! Você acertou o número {numero_correto} em {tentativa_atual} tentativa(s)!")
            return 1  # Retorna 1 ponto por acerto
        elif tentativa < numero_correto:
            print("O número correto é maior. Tente novamente.")
        else:
            print("O número correto é menor. Tente novamente.")

    print(f"Suas {limite_tentativas} tentativas acabaram. O número correto era {numero_correto}.")
    return 0  # Retorna 0 ponto por não acerto

# Chamando a função principal
jogar_adivinhacao()
