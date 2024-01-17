import time

def formatar_tempo(segundos):
    horas, minutos = divmod(segundos, 3600)
    minutos, segundos = divmod(minutos, 60)
    return f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"

def temporizador_contador(tempo, modo):
    if modo == "1":
        for segundos in range(tempo + 1):
            print(formatar_tempo(segundos), end="\r")
            time.sleep(1)
        print("\nContagem concluída!")
    elif modo == "2":
        for segundos in range(tempo, -1, -1):
            print(formatar_tempo(segundos), end="\r")
            time.sleep(1)
        print("\nContagem concluída!")
    else:
        print("Modo não reconhecido. Escolha '1' para temporizador 'progressivo' ou '2' para temporizador 'regressivo'. Comece novamente")

# Solicita ao usuário o modo e o tempo desejado
modo = input("Escolha o modo '1' para temporizador 'progressivo' ou '2' para temporizador 'regressivo'): ").lower()
tempo = int(input("Digite o tempo desejado em segundos: "))

# Chama a função principal
temporizador_contador(tempo, modo)


