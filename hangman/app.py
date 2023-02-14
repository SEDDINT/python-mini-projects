import random
import string
from words import words


def getValidWord(words):
    word = random.choice(words).upper()
    return word


def hangman():

    word = getValidWord(words)
    wordLetters = set(word)
    alpabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 10
    while len(wordLetters) > 0 and lives > 0:
        print('you have used theses letters: ', ' '.join(usedLetters))

        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('current word: ', ' '.join(wordList))

        userLetter = input('Guess a letter: ').upper()
        if userLetter in alpabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives - 1
                print('letter is not in the word')
        elif userLetter in usedLetters:
            print('you have already used that character, try again')
        else:
            print('invalid input!')

    if lives == 0:
        print('you lost :(')
    else:
        print(f'you have guessed the word! {word}')


def main():
    hangman()


if __name__ == '__main__':
    main()
