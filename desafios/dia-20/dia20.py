# Criar uma lista de dicionários para armazenar as perguntas, opções e respostas
quiz = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opções": ["A) Rio de Janeiro", "B) São Paulo", "C) Brasília", "D) Salvador"],
        "resposta": "C",
        "correta": "Brasília"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opções": ["A) William Shakespeare", "B) Miguel de Cervantes", "C) Dante Alighieri", "D) Machado de Assis"],
        "resposta": "B",
        "correta": "Miguel de Cervantes"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opções": ["A) Saturno", "B) Júpiter", "C) Terra", "D) Urano"],
        "resposta": "B",
        "correta": "Júpiter"
    },
    {
        "pergunta": "Qual é o nome do maior osso do corpo humano?",
        "opções": ["A) Fêmur", "B) Úmero", "C) Tíbia", "D) Esterno"],
        "resposta": "A",
        "correta": "Fêmur"
    },
    {
        "pergunta": "Qual é o nome do cientista que formulou a teoria da relatividade?",
        "opções": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileu Galilei", "D) Charles Darwin"],
        "resposta": "B",
        "correta": "Albert Einstein"
    },
    {
        "pergunta": "Qual é o nome da maior floresta tropical do mundo?",
        "opções": ["A) Floresta Amazônica", "B) Floresta do Congo", "C) Floresta de Taiga", "D) Floresta de Borneo"],
        "resposta": "A",
        "correta": "Floresta Amazônica"
    },
    {
        "pergunta": "Qual é o nome do autor do livro 'O Pequeno Príncipe'?",
        "opções": ["A) Antoine de Saint-Exupéry", "B) Lewis Carroll", "C) J. R. R. Tolkien", "D) J. K. Rowling"],
        "resposta": "A",
        "correta": "Antoine de Saint-Exupéry"
    },
    {
        "pergunta": "Qual é o nome do maior rio do mundo em extensão?",
        "opções": ["A) Rio Nilo", "B) Rio Amazonas", "C) Rio Yangtzé", "D) Rio Mississipi"],
        "resposta": "A",
        "correta": "Rio Nilo"
    },
    {
        "pergunta": "Qual é o nome da deusa grega da sabedoria e da guerra?",
        "opções": ["A) Afrodite", "B) Hera", "C) Atena", "D) Ártemis"],
        "resposta": "C",
        "correta": "Atena"
    },
    {
        "pergunta": "Qual é o nome do maior deserto do mundo?",
        "opções": ["A) Deserto do Saara", "B) Deserto da Arábia", "C) Deserto de Gobi", "D) Deserto da Antártida"],
        "resposta": "D",
        "correta": "Deserto da Antártida"
    }
]

# Inicializar a variável para contar as respostas corretas
pontos = 0

# Criar um loop para apresentar as perguntas e obter as respostas do usuário
for i, q in enumerate(quiz):
    # Mostrar a pergunta e as opções
    print(q["pergunta"])
    for o in q["opções"]:
        print(o)
    # Obter a resposta do usuário
    resposta = input("Digite a letra da sua resposta: ").upper()
    # Verificar se a resposta está correta e atualizar a pontuação
    if resposta == q["resposta"]:
        pontos += 1
        print(f"Resposta correta! Você acertou {pontos} de {len(quiz)} perguntas até agora.")
    else:
        print(f"Resposta incorreta. A resposta correta é {q['resposta']} ({q['correta']}). Você acertou {pontos} de {len(quiz)} perguntas até agora.")
    # Mostrar uma linha em branco para separar as perguntas
    print()
    # Verificar se a pergunta atual é a última da lista
    if i == len(quiz) - 1:
        # Mostrar uma mensagem final com a pontuação do usuário
        print(f"O jogo acabou! Você acertou {pontos} de {len(quiz)} perguntas.")
