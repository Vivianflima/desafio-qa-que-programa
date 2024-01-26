import csv
import os
from prettytable import PrettyTable

def criar_arquivo():
    if not os.path.exists('biblioteca.csv'):
        with open('biblioteca.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Índice', 'Título', 'Autor', 'Ano', 'Categoria'])

def adicionar_livro(titulo, autor, ano, categoria):
    with open('biblioteca.csv', 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        # Adicionando um índice incremental automaticamente
        indice = obter_proximo_indice()
        writer.writerow([indice, titulo, autor, ano, categoria])

def visualizar_biblioteca():
    tabela = PrettyTable()
    tabela.field_names = ['Índice', 'Título', 'Autor', 'Ano', 'Categoria']

    with open('biblioteca.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            tabela.add_row(linha)

    print(tabela)

def excluir_livro(indice):
    livros = []

    with open('biblioteca.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            livros.append(linha)

    for livro in livros:
        if indice == livro[0]:
            confirmacao = input(f"Tem certeza que deseja excluir '{livro[1]}'? (s/n): ").lower()
            if confirmacao == 's':
                livros.remove(livro)
                print("Livro excluído com sucesso!")
                break
            else:
                print("Exclusão cancelada.")
                break
    else:
        print("Livro não encontrado.")

    with open('biblioteca.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(livros)

def obter_proximo_indice():
    with open('biblioteca.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        # Obtendo o último índice utilizado, se houver
        indices = [int(linha[0]) for linha in reader if linha[0].isdigit()]

    # Se houver índices, incrementa o último utilizado, senão começa do zero
    return max(indices, default=0) + 1

def obter_opcao_categoria():
    print("\nOpções de Categoria:")
    print("1. Entretenimento - Ficção")
    print("2. Entretenimento - Não Ficção")
    print("3. Tecnologias - Estudos Gerais")
    print("4. Tecnologias - QA ")
    print("5. Outras")

    opcao = input("Escolha uma opção (1/2/3/4/5): ")

    categorias = {
        '1': 'Entretenimento - Ficção',
        '2': 'Entretenimento - Não Ficção',
        '3': 'Tecnologias - Estudos Gerais',
        '4': 'Tecnologias - QA ',
        '5': 'Outras'
    }

    return categorias.get(opcao, 'Outras')

def main():
    criar_arquivo()

    while True:
        print("\n*** Gerenciador de Biblioteca da Vivian ***")
        print("1. Adicionar Livro")
        print("2. Visualizar Biblioteca")
        print("3. Excluir Livro")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = input("Digite o ano de publicação: ")
            categoria = obter_opcao_categoria()

            adicionar_livro(titulo, autor, ano, categoria)
            print("Livro adicionado com sucesso!")

        elif opcao == '2':
            print("\nLista de Livros:")
            visualizar_biblioteca()

        elif opcao == '3':
            indice = input("Digite o índice do livro a ser excluído: ")
            excluir_livro(indice)

        elif opcao == '4':
            print("Fechando Biblioteca.")
            break

        else:
            print("Opção incorreta. Tente novamente.")


if __name__ == "__main__":
    main()
