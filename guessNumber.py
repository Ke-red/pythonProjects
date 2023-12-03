#  guessNumber.py
#  Derek Clarke

#Input: Ask user to guess a number 7 times using the getGuess function
#Processing: Compare user's input against the number variable using the guessWin function
#Output: User's guesses are output as either being higher than the random number, lower than the random number,
#or they are told if the value is invalid, if they guess the number correctly, they are congratulated and asked
#or if they would liek to play again or if they run out of guesses, they are prompted and asked to play again

#Import libraries
import random
first = 1
last = 100

def getGuess(first, last):
    guess = int(input(f'Guess a number between {first} and {last}: '))
    while guess < first or guess > last:
        print ('Invalid entry, try again.')
        guess = int(input(f'Guess a number between {first} and {last}: '))
    return guess

def guessWin(number, guess):
    if guess == number:
        print ('Congratulations, you guessed the correct number!')
        return True
    elif guess > number:
        print (guess, 'is too high')
        return False
    else:
        print (guess, 'is too low')
        return False
    
def main():
    #Intro
    print('Mystery number game!\n')
    #Control Variable
    playAgain = 'y'
    #Generate a new random number for every loop, call getGuess to 
    #ask for the players' guess, then for each guess, 
    #check it by calling for guessWin, if the guess returns true, 
    #break loop and ask to play again, 
    #if loop reaches maximum number of rounds, 
    #print a game over message and ask to play again.
    while playAgain == 'y':
        number = random.randint(first, last)
        rounds = 1
        guess = ''
        while rounds != 8:
            print('Round', rounds, 'of 7\n',
                  '----------------------------')
            guess = getGuess(first, last)
            if guessWin(number, guess) == True:
                break
            rounds += 1
        if rounds == 8:
            print ('You ran out of guesses!\n')    
        playAgain = input('Would you like to play again (y/n)? ')
main()