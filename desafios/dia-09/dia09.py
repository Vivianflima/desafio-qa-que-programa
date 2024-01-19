import random

def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def jogar():
    num_gerado = random.randint(1, 100)
    resposta_correta = is_primo(num_gerado)

    print(f"\nNúmero gerado: {num_gerado}")
    
    while True:
        resposta_usuario = input("É primo? (s/n): ").strip().lower()
        if resposta_usuario == 's' or resposta_usuario == 'n':
            break
        else:
            print("Opção incorreta! Digite 's' para Sim e 'n' para Não. Tente novamente!")

    if resposta_usuario == "s" and resposta_correta or resposta_usuario == "n" and not resposta_correta:
        print(f"\nResposta correta! Você ganhou 1 ponto.")
        return 1
    else:
        print(f"\nResposta incorreta. O jogo acabou.")
        return 0

def ver_pontuacao(pontuacao):
    print(f"\n \nPontuação atual: {pontuacao}")

def zerar_pontuacao():
    return 0

def main():
    pontuacao = 0

    while True:
        print("\n--- Jogo do Número Primo ---")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ").strip()

        if opcao == "1":
            pontuacao += jogar()
        elif opcao == "2":
            ver_pontuacao(pontuacao)
        elif opcao == "3":
            pontuacao = zerar_pontuacao()
            print("Pontuação zerada.")
        elif opcao == "4":
            print("Obrigado por jogar. Até mais!")
            break
        else:
            print("Opção incorreta! Escolha uma opção válida (1/2/3/4).")

if __name__ == "__main__":
    main()

