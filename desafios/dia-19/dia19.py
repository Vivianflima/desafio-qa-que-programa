contatos = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o e-mail do contato: ")

    contato = {"Nome": nome, "Telefone": telefone, "E-mail": email}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    print("\nLista de Contatos:")
    for i, contato in enumerate(contatos, 1):
        print(f"{i}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, E-mail: {contato['E-mail']}")

def buscar_contato():
    nome_busca = input("Digite o nome do contato a ser buscado: ")
    encontrados = []

    for contato in contatos:
        if nome_busca.lower() in contato['Nome'].lower():
            encontrados.append(contato)

    if encontrados:
        print("\nContatos encontrados:")
        for i, contato in enumerate(encontrados, 1):
            print(f"{i}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, E-mail: {contato['E-mail']}")
    else:
        print("Contato não encontrado.")

def excluir_contato():
    nome_excluir = input("Digite o nome do contato a ser excluído: ")
    encontrados = []

    for contato in contatos:
        if nome_excluir.lower() in contato['Nome'].lower():
            encontrados.append(contato)

    if encontrados:
        if len(encontrados) > 1:
            print("\nContatos encontrados:")
            for i, contato in enumerate(encontrados, 1):
                print(f"{i}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, E-mail: {contato['E-mail']}")

            indice = int(input("Digite o número do contato a ser excluído: ")) - 1

            if 0 <= indice < len(encontrados):
                contatos.remove(encontrados[indice])
                print(f"Contato {encontrados[indice]['Nome']} removido com sucesso!")
            else:
                print("Índice inválido. Nenhum contato foi removido.")
        else:
            contatos.remove(encontrados[0])
            print(f"Contato {encontrados[0]['Nome']} removido com sucesso!")
    else:
        print("Contato não encontrado.")

def main():
    while True:
        print("\n*** Agenda de Contatos ***")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Excluir Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            excluir_contato()
        elif opcao == '5':
            print("Fechando Agenda de Contatos.")
            break
        else:
            print("Opção incorreta. Tente novamente.")

if __name__ == "__main__":
    main()
