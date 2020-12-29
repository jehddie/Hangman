import random
import string
from HangmanFiles import drawing, words


def game():
    lives = 5
    word = random.choice(words).upper()
    letters_in_word = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    while lives > 0 and len(letters_in_word) > 0:
        print()

        print('You have used these letters: ', ' '.join(used_letters))

        # Provides hint/help
        word_list = [i if i in used_letters else '_' for i in word]
        print('Current word: ', ' '.join(word_list))

        user_guess = input('Guess a letter: ').upper()

        if user_guess in alphabets - used_letters:
            used_letters.add(user_guess)

            if user_guess in letters_in_word:
                letters_in_word.remove(user_guess)

            else:
                print(f'{user_guess} is not in the word.')
                print(drawing[5 - lives].lstrip('\n'))
                lives -= 1

        # Avoids duplicates
        elif user_guess in used_letters:
            print('You have already used that letter')

        else:
            print('That\'s not a valid letter')

    # When the game is over
    if lives == 0:
        print(f'Sorry you died, the word was {word}')
        print(drawing[4].lstrip('\n'))
    else:
        print(f'Yay! you guessed the word {word}!')


game()
