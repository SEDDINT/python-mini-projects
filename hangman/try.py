import random
import string
from words import words


def theWord(words):
    word = random.choice(words).upper()
    return word


def hangman():
    word = theWord(words)
    wordLetters = set(word)
    alpabetLetters = set(string.ascii_uppercase,)
    usedLetters = set()

    while len(wordLetters) > 0:
        print('you have used these letters: ', ', '.join(usedLetters))
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('current word: ', ' '.join(wordList))

        userLetter = input('guess a letter: ').upper()

        if userLetter in alpabetLetters - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                print('letter is not in the word')
        elif userLetter in usedLetters:
            print('you have already used that character, try again')
        else:
            print('invalid input!')
    print(f'you have guessed the word it was {word}')


def main():
    hangman()


if __name__ == '__main__':
    main()
