# Função para adicionar tarefa à lista
def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para remover tarefa da lista
def remover_tarefa(lista_tarefas, indice):
    if lista_tarefas:
        try:
            tarefa_removida = lista_tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        except IndexError:
            print("Índice inválido. Verifique a posição da tarefa na lista.")
    else:
        print("A lista de tarefas está vazia. Não é possível remover tarefas.")

# Função para listar todas as tarefas
def listar_tarefas(lista_tarefas):
    if lista_tarefas:
        print("Lista de Tarefas:")
        for indice, tarefa in enumerate(lista_tarefas, start=1):
            print(f"{indice}. {tarefa}")
    else:
        print("A lista de tarefas está vazia.")

# Lista para armazenar as tarefas
tarefas = []

# Loop principal
while True:
    # Menu de opções
    print("\n--- Menu ---")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Sair")

    # Solicitar escolha do usuário
    escolha = input("Escolha uma opção (1/2/3/4): ")

    # Processar escolha do usuário
    if escolha == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(tarefas, nova_tarefa)
    elif escolha == "2":
        listar_tarefas(tarefas)
        if tarefas:
            indice_remover = input("Digite o número da tarefa a ser removida: ")
            if indice_remover.isdigit():
                remover_tarefa(tarefas, int(indice_remover) - 1)
            else:
                print("Índice inválido. Digite um número.")
    elif escolha == "3":
        listar_tarefas(tarefas)
    elif escolha == "4":
        print("Saindo... Até logo!")
        break
    else:
        print("Escolha inválida. Tente novamente.")
