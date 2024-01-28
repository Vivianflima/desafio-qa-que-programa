import requests

def obter_taxa_conversao(moeda_origem, moeda_destino):
    endpoint = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'
    resposta = requests.get(endpoint)

    if resposta.status_code == 200:
        taxas = resposta.json()['rates']
        taxa_destino = taxas.get(moeda_destino.upper())

        if taxa_destino:
            return taxa_destino
        else:
            print(f"A moeda de destino {moeda_destino} não é suportada.")
    else:
        print(f"Erro ao obter as taxas de câmbio. Status Code: {resposta.status_code}")

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxa = obter_taxa_conversao(moeda_origem, moeda_destino)

    if taxa:
        valor_convertido = valor * taxa
        return valor_convertido
    else:
        return None

def listar_opcoes_moeda():
    opcoes = {
        "1": "USD - Dólar Americano",
        "2": "EUR - Euro",
        "3": "GBP - Libra Esterlina",
        "4": "JPY - Iene Japonês",
        "5": "CAD - Dólar Canadense",
        "6": "AUD - Dólar Australiano",
        "7": "CHF - Franco Suíço",
        "8": "CNY - Yuan Chinês",
        "9": "SEK - Coroa Sueca",
        "10": "NZD - Dólar da Nova Zelândia",
        "11": "BRL - Real Brasileiro"
    }
    for key, value in opcoes.items():
        print(f"{key}: {value}")
    return opcoes

def main():
    opcoes = listar_opcoes_moeda()
    escolha_origem = input("Escolha o índice da moeda de origem: ")
    while escolha_origem not in opcoes.keys():
        print("Escolha inválida. Por favor, escolha um índice da lista.")
        opcoes = listar_opcoes_moeda()
        escolha_origem = input("Escolha o índice da moeda de origem: ")

    moeda_origem = opcoes[escolha_origem].split(" - ")[0]

    escolha_destino = input("Escolha o índice da moeda de destino: ")
    while escolha_destino not in opcoes.keys():
        print("Escolha inválida. Por favor, escolha um índice da lista.")
        escolha_destino = input("Escolha o índice da moeda de destino: ")

    moeda_destino = opcoes[escolha_destino].split(" - ")[0]

    valor = float(input("Digite o valor a ser convertido: "))
    
    resultado = converter_moeda(valor, moeda_origem, moeda_destino)

    if resultado is not None:
        print(f"Valor convertido: {resultado:.2f} {moeda_destino}")
    else:
        print("Conversão falhou.")

if __name__ == "__main__":
    main()
