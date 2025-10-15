#wordle
import random as r
import pathlib as p
from string import ascii_letters as ASC
from rich.console import Console
from rich.theme import Theme as th
cs = Console(width = 40, theme = th({'warning': 'red on yellow'}))
#for testing
#random.seed(123)
def main():
    word = get_random_word()
    guesses = ['_' * 5] * 6
    # main loop
    for idx in range(6):
        refresh_page(headline = f'Guess nr {idx+1}:')
        show_guesses(guesses, word)
        guesses[idx] = input(f'\nGuess word:').upper()
        if guesses[idx] == word:
            print('Congratulations! You won! The correct word was ' + word)
            break
    else:
        game_over(word)

def refresh_page(headline):
    cs.clear()
    cs.rule(f'[bold blue]:leafy_green: {headline} :leafy_green:[/]\n')

def get_random_word():
    word_list = p.Path(__file__).parent / 'wordlist.txt'
    words = [word.upper()
             for word in word_list.read_text(encoding = 'utf-8').split('\n')
             if len(word) == 5 and all(letter in ASC for letter in word)]
    return r.choice(words)

def show_guesses(guesses, word):
    for g in guesses:
        styled_g = []
        for letter, correct in zip(g, word):
            if letter == correct:
                style = 'bold white on green'
            elif letter in word: 
                style = 'bold white on yellow'
            elif letter in ASC:
                style = 'white on #666666' #grey
            else:
                style = 'dim' #placeholders
            styled_g.append(f'[{style}]{letter}[/]')
        cs.print(''.join(styled_g), justify = 'center')

def game_over(x):
    print(f'Sorry! You ran out of guesses. The correct word was {x}')        

if __name__ == '__main__': # execute
    main()