# Resolvedor de Palavras (Termo/Wordle) em Python

> Um agente autônomo que utiliza um algoritmo de lógica de eliminação para resolver o jogo de palavras Termo (ou Wordle) de forma eficiente.

Este projeto foi desenvolvido para aplicar conceitos de algoritmos e estruturas de dados na resolução de um problema lógico conhecido. O objetivo é adivinhar a palavra correta no menor número de tentativas possível, processando o feedback de cada palpite para tomar decisões mais inteligentes.

---

### ✨ Estratégia do Algoritmo

O bot funciona com base em um processo contínuo de filtragem de um dicionário de palavras. A cada rodada, ele refina a lista de palavras candidatas com base no feedback recebido (`GREEN`, `YELLOW`, `RED`).

1.  **Letras Corretas (GREEN):** Qualquer letra confirmada em uma posição é armazenada. A lista de palavras possíveis é imediatamente filtrada para conter apenas palavras que tenham essa letra naquela exata posição.

2.  **Letras Presentes (YELLOW):** Letras que existem na palavra, mas estão na posição errada, são adicionadas a um conjunto de "letras obrigatórias". Além disso, a posição incorreta é registrada. A lista de palavras é filtrada para:
    * Incluir apenas palavras que contenham todas as letras "obrigatórias".
    * Excluir palavras que tenham essas letras na posição incorreta já testada.

3.  **Letras Ausentes (RED):** Letras que não pertencem à palavra são adicionadas a um conjunto de "letras inválidas". A lista de palavras é filtrada para remover qualquer palavra que contenha essas letras.
    * **Caso Especial:** O algoritmo também trata o caso de letras repetidas, onde uma ocorrência pode ser `YELLOW` e outra `RED`. Nesse cenário, a letra não é totalmente invalidada, mas sim registrada como inválida para aquela posição específica.

O palpite seguinte é escolhido aleatoriamente dentre a lista de palavras restantes, que já foi drasticamente reduzida pela lógica.

---

### 🛠️ Tecnologias e Conceitos

* **Python:** Linguagem principal para a implementação da lógica.
* **Estruturas de Dados:** Uso de **listas** e **conjuntos (sets)** para gerenciar com eficiência as palavras possíveis, letras confirmadas, presentes e inválidas.
* **Algoritmos:** Implementação de um algoritmo de filtragem e redução de espaço de busca.

---

### 🚀 Como Executar

*Utilize python game.py para jogar o jogo manualmente e python tournament.py para executar uma simulação de 500 partidas com o algoritmo*
