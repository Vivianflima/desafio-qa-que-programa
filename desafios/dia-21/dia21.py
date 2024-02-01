class ConsultaSQLBuilder:
    def __init__(self):
        self.tipo_consulta = None
        self.colunas = []
        self.tabela = None
        self.condicoes = {}

    def criar_consulta_select(self):
        self.tipo_consulta = "SELECT"
        self.colunas = input("Digite as colunas separadas por vírgula: ").split(", ")
        self.tabela = input("Digite o nome da tabela: ")
        self.condicoes = input("Digite as condições WHERE (separadas por AND): ").split(" AND ")

    def criar_comando_update(self):
        self.tipo_consulta = "UPDATE"
        self.tabela = input("Digite o nome da tabela: ")
        self.colunas = input("Digite as colunas e novos valores (ex: coluna1 = valor1, coluna2 = valor2): ").split(", ")
        self.condicoes = input("Digite as condições WHERE (separadas por AND): ").split(" AND ")

    def criar_comando_insert(self):
        self.tipo_consulta = "INSERT"
        self.tabela = input("Digite o nome da tabela: ")
        self.colunas = input("Digite as colunas (separadas por vírgula): ").split(", ")
        self.valores = input("Digite os valores correspondentes (separados por vírgula): ").split(", ")

    def gerar_consulta(self):
        if self.tipo_consulta == "SELECT":
            consulta = f"SELECT {', '.join(self.colunas)} FROM {self.tabela}"
            if self.condicoes:
                consulta += f" WHERE {' AND '.join(self.condicoes)}"
            print(f"Consulta SQL gerada: {consulta}")
        elif self.tipo_consulta == "UPDATE":
            comando = f"UPDATE {self.tabela} SET {', '.join(self.colunas)}"
            if self.condicoes:
                comando += f" WHERE {' AND '.join(self.condicoes)}"
            print(f"Comando SQL UPDATE gerado: {comando}")
        elif self.tipo_consulta == "INSERT":
            comando = f"INSERT INTO {self.tabela} ({', '.join(self.colunas)}) VALUES ({', '.join(self.valores)})"
            print(f"Comando SQL INSERT gerado: {comando}")


def main():
    builder = ConsultaSQLBuilder()

    while True:
        print("\nMenu:")
        print("1. Criar Consulta SQL SELECT")
        print("2. Criar Comando SQL UPDATE")
        print("3. Criar Comando SQL INSERT")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            builder.criar_consulta_select()
            builder.gerar_consulta()
        elif opcao == "2":
            builder.criar_comando_update()
            builder.gerar_consulta()
        elif opcao == "3":
            builder.criar_comando_insert()
            builder.gerar_consulta()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
