# Dia 10: Jogo da Adivinhação

## Desafio

Desenvolva um jogo de adivinhação em que o usuário deve adivinhar um número gerado aleatoriamente pelo programa. O jogo deve ter as seguintes características:

- O programa gera um número aleatório entre 1 e 100.
- O jogador tem um número limitado de tentativas (7) para adivinhar o número correto.
- Após cada tentativa, o programa fornece dicas sobre se o número correto é maior ou menor do que a tentativa atual do jogador.
- O jogo continua até que o jogador adivinhe corretamente o número ou esgote todas as tentativas.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?

- **Geração de Números Aleatórios:** Use o módulo random para gerar números aleatórios.
- **Input do jogador e Loops:** Crie um loop para permitir que o jogador faça várias tentativas.
- **Condicionais:** Use estruturas condicionais para fornecer dicas ao jogador com base em suas tentativas.

## Dica importante

- Sempre forneça feedback ao jogador após cada tentativa, dizendo se o número correto é maior, menor ou igual à sua tentativa atual.
- A cada tentativa, além do feedback, ele mostra quantas tentativas o jogador ainda tem.
- Ao final do jogo, informe quantas tentativas o jogador levou para adivinhar o número correto e se ele venceu ou perdeu.
- A cada acerto, ele ganha um ponto.
- Crie um menu inicial que contém opções para Jogar, Ver Pontuação, Zerar Pontuação e Sair.

## Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```bash
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

- **TESTE 01:** O programa gera o número 42. O jogador chuta 50. O programa fornece a dica "O número é menor." O jogador chuta 30. O programa fornece a dica "O número é maior." O jogador chuta 40. O programa fornece a dica "O número é maior." O jogador chuta 41. O programa fornece a dica "O número é maior." O jogador chuta 42. O programa informa que o jogador acertou, ele ganha 1 ponto e mostra quantos pontos ele tem.
- **TESTE 02:** O programa gera o número 67. O jogador faz 7 tentativas sem sucesso. O programa informa que o jogador perdeu, mas o jogo não é encerrado.
- **TESTE 03:** O jogador pede para ver sua pontuação.
- **TESTE 04:** O jogador pede para zerar sua pontuação.
- **TESTE 05:** O jogador pede para sair do jogo.

Você pode fazer outros testes caso ache necessário.
