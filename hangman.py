#Hangman


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    wordlength = len(secretWord)
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
    
    if count == wordlength:
        return True
    else:
        return False
            


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = []
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word.append(letter)
        else:
            guessed_word.append('_ ')
    return ''.join(guessed_word)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet.remove(letter)
    return ''.join(alphabet)

#print (getAvailableLetters(['a', 'b', 'r']))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #initiate game with guesses number and letters guessed list
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    lettersGuessed = []
    guess_number = 8
    mistake_number = 0
    #game functions while guesses aren't 0 or another break happens
    while guess_number > 0:
        #if word not guessed, continue
        if isWordGuessed(secretWord, lettersGuessed) == False:
            print('------------')
            print('You have ' + str(guess_number) + ' guesses left')
            print('Available letters: ' + getAvailableLetters(lettersGuessed))
            
            guess = input('Please guess a letter:')
            guess = guess.lower()
            #sanitize guess
            #if guess == '':
                
            
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print('Oops! You\'ve already guessed that letter:' + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                lettersGuessed.append(guess)
                guess_number -= 1
                mistake_number += 1
                #if run out of guesses, end
                if guess_number == 0:
                    print('-----------')
                    print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')
                    return
        #if word is guessed halt
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print('-----------')
            print('Congratulations, you won!')
            return
        
        
wordlist = loadWords()
word = chooseWord(wordlist)
wordtest = 'a'
start = print(hangman(word))




# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
