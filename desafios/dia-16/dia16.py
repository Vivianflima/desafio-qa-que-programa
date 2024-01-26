import random
from unidecode import unidecode

def escolher_palavra():
    palavras = ["banana", "qualidade", "desafio", "Agilidade", "prevenção", "colaboração", "amigos"]
    return random.choice(palavras)

def remover_acentuacao(letra):
    return unidecode(letra)

def ocultar_palavra(palavra, letras_corretas):
    return ''.join(letra if remover_acentuacao(letra) in letras_corretas else '_' for letra in palavra)

def jogar_forca():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = set()
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas < tentativas_maximas:
        palavra_oculta = ocultar_palavra(palavra_secreta, letras_corretas)
        print(f"\nPalavra: {palavra_oculta}")
        print(f"Tentativas restantes: {tentativas_maximas - tentativas}")
        tentativa = remover_acentuacao(input("Digite uma letra: ").lower())

        if tentativa in letras_corretas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if tentativa in unidecode(palavra_secreta):
            print("Letra correta!")
            letras_corretas.add(tentativa)
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas += 1

        if set(letras_corretas) == set(unidecode(palavra_secreta)):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
            break

    else:
        adivinhar_palavra = input("\nÚltima tentativa! Você quer adivinhar a palavra completa? (s/n): ").lower()
        if adivinhar_palavra == 's':
            tentativa_palavra = remover_acentuacao(input("Digite a palavra completa: ").lower())
            if tentativa_palavra == unidecode(palavra_secreta):
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
            else:
                print(f"\nFim de jogo! A palavra era: {palavra_secreta}")
        else:
            print(f"\nFim de jogo! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogar_forca()
