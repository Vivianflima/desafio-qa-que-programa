# Dia 11: Ordenação de Lista

## Desafio
Desenvolva um script que ordene uma lista de números fornecida pelo usuário.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- **Algoritmos de Ordenação:** Aprenda algoritmos básicos de ordenação como `sort()` e `sorted()`.
- **Listas em Python:** Pratique a manipulação de listas.
- **Input do Usuário e Loops:** Crie um loop para permitir que o usuário informe todos os números que quer adicionar à lista.

## Dica importante
- Existem diferentes algoritmos de ordenação, mas para este desafio, você pode começar usando a função `sorted()` ou o método `sort()` para ordenar a lista fornecida pelo usuário.
- Certifique-se de receber a lista do usuário como entrada e, em seguida, use a função de ordenação para classificar os números na lista.
- Considere a diferença entre `sorted()` e `sort()` e escolha o método que melhor se adapta às suas necessidades.
- O usuário deve poder adicionar os números de maneira fácil, informando número a número.
- O usuário deve ter uma opção para dizer que terminou de inserir os números para que o algoritmo possa ordenar os números.

## Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```bash
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

```bash
TESTE 01: Ordene a lista [5, 2, 9, 1, 5, 6] -> Resultado esperado: [1, 2, 5, 5, 6, 9]
TESTE 02: Ordene a lista [-10, 100, 42, 0, -5, 8] -> Resultado esperado: [-10, -5, 0, 8, 42, 100]
TESTE 03: Ordene a lista [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] -> Resultado esperado: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
TESTE 04: Ordene a lista vazia [] -> Resultado esperado: []
```

Você pode fazer outros testes caso ache necessário.