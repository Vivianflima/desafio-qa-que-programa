<<<<<<< HEAD
=======

>>>>>>> c7ab1796d6393ed1db74aefe3e841c8d8b04fe7e
# Desafio QA Que Programa - Desafio 4

## Dia 4: Contador de Palavras

### Desafio
Desenvolva um programa que conte o número de palavras em um texto fornecido pelo usuário. O programa deve ser capaz de separar as palavras em um texto e determinar quantas palavras estão presentes.

### Conhecimentos Necessários
Para resolver este desafio, é recomendado adquirir conhecimentos nos seguintes tópicos:

- **Manipulação de Strings:** Você precisará entender como usar funções de strings, como `split()`, para separar o texto em palavras.
- **Laços de repetição (for ou while):** Utilize laços de repetição para percorrer as palavras e contar a quantidade.

### Dica Importante
Use a função `split()` para dividir o texto em palavras. Por padrão, essa função divide o texto em palavras separadas por espaços em branco.
Considere que números e caracteres especiais são considerados palavras. Por exemplo, "Oi, " e "18 anos", a vírgula e o número 18 são considerados palavras. Nestes dois exemplos, o seu código deveria retornar 2 palavras.
Relaxe em relação ao plural de "palavra" na saída do seu código (TESTE 09) no caso do número de palavras do texto ser 1. Não precisa se preocupar em tratar o texto para imprimir no singular caso a contagem seja 1, mas pode ser um plus que você pode implementar no seu código caso deseje.

### Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo:

```bash
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

- **TESTE 01:** "Isso é um teste." -> O texto contém 4 palavras.
- **TESTE 02:** "   Olá,    mundo!   " -> O texto contém 2 palavras.
- **TESTE 03:** "Palavra Palavra palavra" -> O texto contém 3 palavras.
- **TESTE 04:** "Este é um teste de contagem de palavras." -> O texto contém 8 palavras.
- **TESTE 05:** "" -> O texto contém 0 palavras.
- **TESTE 06:** "Maria tem 10 anos." -> O texto contém 4 palavras.
- **TESTE 07:** "Olá ,  Mundo" -> O texto contém 3 palavras.
- **TESTE 08:** "Em uma tarde ensolarada, 3 crianças brincavam no parque. [...]" -> O texto contém 151 palavras.
- **TESTE 09:** "Oi" -> O texto contém 1 palavra.

Sinta-se à vontade para realizar outros testes caso ache necessário. 
