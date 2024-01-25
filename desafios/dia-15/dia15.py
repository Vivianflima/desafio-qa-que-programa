import csv
from prettytable import PrettyTable

categorias = {
    '1': 'Entretenimento - Ficção',
    '2': 'Entretenimento - Não Ficção',
    '3': 'Tecnologias - Estudos Gerais',
    '4': 'Tecnologias - QA (Garantia de Qualidade)',
    '5': 'Outras'
}

def carregar_biblioteca():
    try:
        with open('biblioteca.csv', 'r', newline='', encoding='latin-1') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            return list(leitor_csv)
    except FileNotFoundError:
        return []

def salvar_biblioteca(biblioteca):
    with open('biblioteca.csv', 'w', newline='', encoding='latin-1') as arquivo_csv:
        colunas = ['Índice', 'Título', 'Autor', 'Ano', 'Categoria']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=colunas)
        escritor_csv.writeheader()
        escritor_csv.writerows(biblioteca)

def visualizar_biblioteca(biblioteca):
    if not biblioteca:
        print("A biblioteca está vazia.")
        return

    tabela = PrettyTable()
    tabela.field_names = ['Índice', 'Título', 'Autor', 'Ano', 'Categoria']

    for livro in biblioteca:
        tabela.add_row([livro['Índice'], livro['Título'], livro['Autor'], livro['Ano'], livro['Categoria']])

    print(tabela)

def selecionar_categoria():
    print("\nSelecione a categoria:")
    for chave, valor in categorias.items():
        print(f"{chave}. {valor}")

    while True:
        escolha_categoria = input("Escolha a categoria (1/2/3/4/5): ")
        if escolha_categoria in categorias:
            return categorias[escolha_categoria]
        else:
            print("Categoria inválida. Tente novamente.")

def excluir_livro(biblioteca):
    visualizar_biblioteca(biblioteca)
    indice_excluir = input("\nDigite o índice do livro que deseja excluir: ")

    if indice_excluir.isdigit():
        indice_excluir = int(indice_excluir)
        if 1 <= indice_excluir <= len(biblioteca):
            confirmacao = input(f"Tem certeza que deseja excluir o livro '{biblioteca[indice_excluir - 1]['Título']}'? (s/n): ").lower()
            if confirmacao == 's':
                livro_excluido = biblioteca.pop(indice_excluir - 1)
                print(f"\nLivro '{livro_excluido['Título']}' excluído com sucesso!")
            else:
                print("\nExclusão cancelada.")
        else:
            print("\nÍndice inválido. Tente novamente.")
    else:
        print("\nÍndice inválido. Tente novamente.")

def main():
    biblioteca = carregar_biblioteca()

    while True:
        print("\n-------- Gerenciador de Biblioteca da Vivian --------")
        print("1. Adicionar livro")
        print("2. Visualizar biblioteca")
        print("3. Excluir livro")
        print("4. Sair")

        escolha = input("Escolha a opção (1/2/3/4): ")

        if escolha == "1":
            adicionar_livro(biblioteca)
        elif escolha == "2":
            visualizar_biblioteca(biblioteca)
        elif escolha == "3":
            excluir_livro(biblioteca)
        elif escolha == "4":
            salvar_biblioteca(biblioteca)
            print("Fechando biblioteca da Vivian.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
