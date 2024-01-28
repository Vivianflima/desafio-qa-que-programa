import csv
import os
from datetime import datetime

def criar_arquivo():
    if not os.path.exists('despesas.csv'):
        with open('despesas.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Data', 'Valor', 'Descrição', 'Categoria'])

def registrar_despesa():
    data = input("Digite a data (formato DD/MM/AAAA): ")
    valor = input("Digite o valor da despesa: ")
    descricao = input("Digite a descrição da despesa: ")
    categoria = selecionar_categoria()

    # Substituir a vírgula por ponto e converter para float
    valor = float(valor.replace(',', '.'))

    with open('despesas.csv', 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([data, valor, descricao, categoria])

    print("Despesa registrada com sucesso!")

def selecionar_categoria():
    categorias = ['Alimentação', 'Transporte', 'Educação', 'Lazer', 'Outros']

    print("\nCategorias Disponíveis:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")

    while True:
        try:
            escolha = int(input("Escolha a categoria (1 a 5): "))
            if 1 <= escolha <= 5:
                return categorias[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

def resumo_por_categoria():
    categorias = {'Alimentação': 0, 'Transporte': 0, 'Educação': 0, 'Lazer': 0, 'Outros': 0}

    with open('despesas.csv', 'r') as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            categoria = linha['Categoria']
            valor = float(linha['Valor'])
            categorias[categoria] += valor

    print("\nResumo de Despesas por Categoria:")
    for categoria, total in categorias.items():
        print(f"{categoria}: R${total:.2f}")

def resumo_por_data():
    data_desejada = input("Digite a data desejada (formato DD/MM/AAAA): ")

    total_despesas = 0
    with open('despesas.csv', 'r') as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            if linha['Data'] == data_desejada:
                total_despesas += float(linha['Valor'])

    print(f"\nTotal de Despesas em {data_desejada}: R${total_despesas:.2f}")

def main():
    criar_arquivo()

    while True:
        print("\n*** Calculadora de Despesas Pessoais ***")
        print("1. Registrar Despesa")
        print("2. Resumo por Categoria")
        print("3. Resumo por Data")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            registrar_despesa()
        elif opcao == '2':
            resumo_por_categoria()
        elif opcao == '3':
            resumo_por_data()
        elif opcao == '4':
            print("Fechando Calculadora de Despesas Pessoais.")
            break
        else:
            print("Opção incorreta. Tente novamente.")

if __name__ == "__main__":
    main()
