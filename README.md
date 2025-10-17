# Wordle Solver - Resolvedor de Palavras em Python

> Um módulo de lógica em Python que implementa um algoritmo de eliminação para resolver de forma autônoma jogos de palavras como Termo/Wordle.

Este repositório contém o "cérebro" de um jogador de Wordle. O arquivo principal, `player.py`, foi projetado para ser importado e executado por um ambiente de simulação (`game.py` para jogos únicos e `tournament.py` para testes em massa), recebendo o histórico de jogadas e feedbacks para decidir o próximo palpite.

---

### ✨ A Estratégia do Algoritmo

O núcleo da função `player` é um processo de redução de espaço de busca. A cada rodada, o universo de palavras possíveis é drasticamente filtrado com base nas regras inferidas do feedback anterior.

1.  **Primeiro Palpite Estratégico:** O jogo começa com uma palavra de alta probabilidade (como "AUREO", "AUDIO") para maximizar a descoberta de vogais e consoantes comuns.

2.  **Processamento de Feedback:** Após cada palpite, o feedback é processado para construir um conjunto de regras:
    * `GREEN` (Letra Correta): A letra e sua posição são salvas. A lista de palavras é imediatamente filtrada para conter apenas aquelas que correspondem a este padrão.
    * `YELLOW` (Letra Presente): A letra é adicionada a um conjunto de "letras obrigatórias", e sua posição atual é marcada como inválida para aquela letra.
    * `RED` (Letra Ausente): A letra é adicionada a um conjunto de "letras proibidas". O algoritmo também trata de forma inteligente o caso de letras repetidas, garantindo que uma letra não seja globalmente proibida se outra instância dela for `GREEN` ou `YELLOW`.

3.  **Filtragem e Próximo Palpite:** Um loop varre a lista de palavras candidatas restantes, e qualquer palavra que viole uma das regras recém-criadas é eliminada. O próximo palpite é então escolhido aleatoriamente da lista refinada e muito menor de palavras possíveis.

Este ciclo se repete, com a lista de possibilidades diminuindo exponencialmente a cada passo, até que a palavra correta seja encontrada.

---

### 🛠️ Tecnologias e Conceitos

* **Python:** Linguagem principal para a implementação da lógica.
* **Design Modular:** A função `player` foi projetada para ser autônoma e sem estado, recebendo toda a informação necessária como parâmetros, permitindo que seja facilmente testada e integrada.
* **Estruturas de Dados:** Uso de **listas** e, crucialmente, **conjuntos (`sets`)** para gerenciar as regras de validação (letras presentes, ausentes, posições inválidas) de forma computacionalmente eficiente.
* **Algoritmos:** Implementação de um algoritmo de filtragem e redução de espaço de busca.

---

### 🚀 Como Executar

Este projeto foi desenhado para ser executado através dos scripts `game.py` (partida única) e `tournament.py` (múltiplas partidas).

**Executar uma partida única (com visualização):**
```bash
python game.py --lang pt
```
*(Use `--lang` para escolher o idioma: `en`, `pt`, `fr`, `es`, `it`)*

**Executar um torneio de simulação (sem visualização):**
```bash
python tournament.py --lang pt --num_games 100
```
