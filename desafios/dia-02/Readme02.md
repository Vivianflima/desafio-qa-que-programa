# Desafio QA Que Programa - Desafio 2

## Dia 2: Calculadora Básica

### Desafio
Desenvolva um programa que realize operações básicas de matemática, como adição, subtração, multiplicação e divisão.

### Conhecimentos Necessários
Para resolver este desafio, é recomendado adquirir conhecimentos nos seguintes tópicos:

- **Operações Matemáticas em Python:** Conheça como realizar operações matemáticas básicas usando os operadores `+`, `-`, `*` e `/`.
- **Input e Output:** Aprenda a receber entrada do usuário usando `input()` e mostrar resultados.

### Dica Importante
Ao lidar com o valor inserido pelo usuário, é crucial considerar que tudo que o usuário insere vem como String. Portanto, para realizar adição, subtração, multiplicação e divisão do número recebido, será necessário converter a String recebida para um inteiro ou para float (se quiser que sua calculadora faça contas com números decimais).

Lembre-se de que float em Python é utilizado com ponto `.` e não vírgula `,` (por exemplo, `2.5` e não `2,5`). Você pode fazer um tratamento extra no seu código se quiser evitar que o uso da vírgula cause um erro de código, mas faça apenas se quiser tentar algo a mais, para o desafio não é necessário.

Você pode fazer alguns tratamentos para lidar com casos do tipo divisão por 0.

### Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo:

```bash
python dia02.py.py
```

Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

- **TESTE 01:** `1 + 5` -> `6`
- **TESTE 02:** `5 - 1` -> `4`
- **TESTE 03:** `2 x 30` -> `60`
- **TESTE 04:** `21 / 7` -> `3`
- **TESTE 05:** `10 / 0` -> Não é possível dividir por zero
- **TESTE 06:** `1 + -5` -> `-4`
- **TESTE 07:** `5 - -1` -> `6`
- **TESTE 08:** `2 x -30` -> `-60`
- **TESTE 09:** `-21 / 7` -> `-3`
- **TESTE 10:** `-10 / 0` -> Não é possível dividir por zero

Sinta-se à vontade para realizar outros testes caso ache necessário. Boa sorte!