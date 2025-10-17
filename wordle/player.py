"""
Implemente aqui o seu código para adivinhar a palavra.

Seu principal objetivo é implementar a função `player`, que deve retornar uma palavra (string) como seu próximo palpite.
Caso sua função não retorne uma string, a automatização não irá ocorrer tanto em game.py quanto em tournament.py.
Caso sua função retorne a string vazia, você poderá jogar manualmente (teclado).

Observações:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
- A função recebe duas listas como argumento:
    - guess_hist: lista de palavras que foram chutadas anteriormente
    - res_hist: lista de respostas dos chutes anteriores
- A função deve retornar uma string como palpite

Lembretes:
- Segue a coloração possíveis dos caracteres:
    - Correto: verde ("GREEN")
    - Presente mas na posição errada: amarelo ("YELLOW")
    - Ausente: vermelho ("RED")
    
Para mais informações, reveja o README.md
"""

import random
from utils import load_words, ALL_COLORS, load_words

WORDS = load_words()

possible_words = [word for word in WORDS if len(word) == 5]  # words size 5

confirmed_char = [None] * 5       # Green list


def player(guess_hist, feedback_hist):
    """ Function that will run the game automatically.

Has last guessing input and last feedback that informs: 
> existing letters in the word (green)
> letters not existing in the word (red)
> letters with wrong position but present in the word (yellow)

Based on feedback, words are retained and others are discarded in the total list of words
"""

    global possible_words
    global confirmed_char

# first guess depending on the language. Good words in each language
    if guess_hist == []:
        if 'AUREO' in possible_words:
            guess = 'AUREO'
        if 'AUDIO' in possible_words:
            guess = 'AUDIO'
        if 'ACIER' in possible_words:
            guess = 'ACIER'
        if 'ARIES' in possible_words:
            guess = 'ARIES'
        if 'ADIPE' in possible_words:
            guess = 'ADIPE'
        return guess

# for the other guesses
    else:
        last_guess = guess_hist[-1]
        last_feedback = feedback_hist[-1]
        # Letters that exist in the word but don't know the position (yellow)
        present_char = set()
        invalid_char = set()                   # Letters that are not in the word (red)

# List of 5 sets in which the letters that cannot be in that position will be put, such that each set represents a position
        invalid_positions = [set(), set(), set(), set(), set()]

# Position of the letter and its corresponding feedback
        for i in range(5):
            guess_char = last_guess[i]
            feedback_char = last_feedback[i]

            if feedback_char == 'GREEN':
                confirmed_char[i] = guess_char
            elif feedback_char == 'YELLOW':
                present_char.add(guess_char)
                invalid_positions[i].add(guess_char)
            elif feedback_char == 'RED':
                fakered = False
                for j in range(5):
                    if last_guess[j] == guess_char and last_feedback[j] != "RED":
                        invalid_positions[i].add(guess_char)
                        fakered = True
                if fakered == False:
                    invalid_char.add(guess_char)

        # iteration of words by the feedback criterion
        new_possibilities = []
        for word in possible_words:
            ok = True

            for char in range(5):
                if word[char] != confirmed_char[char] and confirmed_char[char] != None:
                    ok = False
                    break

                if word[char] in invalid_positions[char]:
                    ok = False
                    break

                if word[char] in invalid_char:
                    ok = False
                    break

                if not present_char.issubset(set(word)):
                    ok = False
                    break

            if ok:                          # all conditions true for a word
                new_possibilities.append(word)

        possible_words = new_possibilities

    guess = random.choice(possible_words)
    return guess