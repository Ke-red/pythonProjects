#   Derek Clarke
#
#   vingtEtUn.py
#
#   Vingt-et-un is a dice game similar to blackjack. The player and the computer roll a dice to start, and then then player take their turn rolling the dice trying to get as close
#   to 21 as possible without going over. The winner is the person who has the highest total at the end of both turns, or whoever did not bust.
#
#   Input: Take the player's name, their menu choices, and when playing the game, their decisions on whether they would like to hit or stay with their totals. Ask user for input to 
#   play again after the game is over.
#
#   Processing: When the player chooses to play Vingt-et-Un, they are presented with the initial roll of their die and the computer's die. They are then prompted to either hit or
#   stay. If they hit, the die are rolled and the rolls are added into the sum of all of their rolls. They can keep hitting until they are satisfied or they bust. If they stay, then
#   it shift's to the computer's turn, where they will roll until they get to 17 or above, where they will automatically stay. The winner is determined by who has the highest number
#   at the end of the computer's turn, or whoever doesn't bust. 21 is the highest you can go without busting, but is not an automatic win, the computer can still tie you. If either
#   the computer or the player's total is over 14 at the end of a round, they will be forced to only roll 1 die until the player either 1. stays 2. gets 21 or 3. busts. The computer
#   will continue to roll 1 dice until it either 1. gets to 17 or greate so it will stay, 2. gets 21 or 3. busts. The total between the two players is calculated and based on a few
#   conditions, will determine the winner.
#
#   Output: When the player types in their name, they are presented a menu where if they choose option 1 in the menu, they are output the rules of the game. When choosing option 2, 
#   they are output their dice rolls based on their decisions, and the computer's dice rolls. Depending on the outputted totals, the winner is determined and a message of who won
#   is output, a tie message is output to the player if him and the computer tie, or a bust message is output based on who busts.


#Import modules, random for the dice rolls and time to put a little time between each dice roll, so the program does not just spit them all out at once instantly. 
import random
import time
game = 'Vingt-et-un'
compName = 'House'

#Introduction function, asks for player's name and greets them, returning the playerName function
def gameIntro():
    playerName = str(input('Type your name: '))
    print (f'\nWelcome, {playerName} to {game}')
    print ('-'*30)
    return playerName

#Rules of the game function, gets called when player selects 1 as their menu option.
def gameRules():
    print(f'\nRules of {game}')
    print('-'*110)
    print('The goal of the game is to get as close to or equal to 21 as possible without going over.\n',
           '\nThe two players take turns throwing two die as many times as desired and add the number thrown each round.\n',
           '\n\t1. A player who totals over 21 is bust and loses.\n',
           '\t2. The player closest to 21 after both players have had a turn, wins.\n',
           '\t3. If the totals for both players are equal, the game is tied.')
    print('\nThe game is over at the end of a round when:\n',
           '\n\t1. One or both players are bust.\n',
           '\t2. Both players choose to stay.')
    print('-'*110)

#The function that controls the whole game, controlling the calls for dice rolls, the ehile loops for each player's turn,    
def gamePlay(playerName):
    #Print's the name of the game
    print(f"\n{game}")
    print(f'-'*27)
    #Defines lists to hold the rolls for the player and computer.
    playerRolls = []
    compRolls = []
    
    #Does an initial dice roll, prints those rolls, then tells the player it is their turn.
    print('\nRolling inital dice...')
    time.sleep(1.5)
    playerDice(playerRolls)
    compDice(compRolls) 
    score(playerName, compName, playerRolls, compRolls)
    print (f'\n{playerName}\'s Turn')
    
    #While loop, that while the sum of the playerRolls list is less than 21, keep asking to hit until they either stand or bust.
    while sum(playerRolls) < 21:
        playerState = str(input('\nDo you want to hit or stand? '))
        #As long as the player keeps hitting, the dice will roll and display their new total every hit. 
        if playerState == 'hit':
            playerDice(playerRolls)
            print('\nRolling dice..')
            time.sleep(1.5)
            score(playerName, compName, playerRolls, compRolls)
        #If player stands, break the loop.
        elif playerState == 'stand':
            break
        #Input validation.
        else:
            print('\nInvalid input. Please enter hit or stand.')
            
    #While loop, if the sum of the compRolls list is less than 17, allow it to keep rolling until it goes over 17, displaying the new total for each roll. 
    while sum(compRolls) < 17:
        
        #If the sum of the playerRolls list is greater than 21, break the loop because the player loses. 
        if sum(playerRolls) > 21:
            print(f'\n{playerName} busted!')
            break
        compDice(compRolls)
        print (f'\n{compName} is rolling..')
        time.sleep(1.5)
        score(playerName, compName, playerRolls, compRolls)
    #If the sum of both lists is equal after all rolls are finished, players tie.   
    if sum(playerRolls) == sum(compRolls):
        print (f'\n{playerName} tied with {compName}!')
    #If the sum of the playerRolls list is less than 21 but the compRolls list goes over 21, the computer busts.
    elif sum(playerRolls) < 21 and sum(compRolls) > 21:
        print (f'\n{compName} busted, {playerName} wins!')
    #If the sum of the playerRolls lis is less that that of the compRolls list, and the compRolls list is less than or equal to 21, the player loses.
    elif sum(playerRolls) < sum(compRolls) and sum(compRolls) <= 21:
        print(f'\n{playerName} lost to {compName}')
    #If the sum of the playerRolls list is more than that of the compRolls list, and the playerRolls list is less than or equal to 21, the player wins.
    elif sum (playerRolls) > sum(compRolls) and sum(playerRolls) <= 21:
        print(f'\n{playerName} beat {compName}')  
        
#Dice roll funtion for the player, as long as the sum of playerRolls list is below 14, roll two seperate die, if over 14, roll a single die.                    
def playerDice(playerRolls):
    if sum(playerRolls) < 14:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        playerRolls.append(roll1)
        playerRolls.append(roll2)
    else:
        roll1 = random.randint(1,6)
        playerRolls.append(roll1)
    return playerRolls

#Dice roll function for the computer, as long as the sum of compRolls list is below 14, roll two seperate die, if over 14, roll a single die.              
def compDice(compRolls):    
    if sum(compRolls) < 14:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        compRolls.append(roll1)
        compRolls.append(roll2)
    else:
        roll1 = random.randint(1,6)
        compRolls.append(roll1)
    return compRolls

#Function to display the rolls of each player after each round. 
def score(playerName, compName, playerRolls, compRolls):
    print(f'\n{playerName:<10}', f'{compName:<10}')  
    print(f'{sum(playerRolls):<10}', f'{sum(compRolls):<10}')
    
def main():
    #Run gameIntro function to greet player and get their name,
    playerName = gameIntro()
    #Control variable.
    playAgain = 'y'
    while playAgain == 'y':
        print('\nOptions:\n',
              '\t1. See the rules\n',
              f'\t2. Play {game}\n',
              '\t3. Quit')
        playerChoice = int(input('\nPick an option: '))
        #Invoke the gameRules function above.
        if playerChoice == 1:
            gameRules()
        #Invoke the gamePlay function above.
        elif playerChoice == 2:
            gamePlay(playerName)
            
            #Ask if player wants to play again.
            playAgain = str(input('\nWould you like to play again (y/n)? '))

        #Break loop if option 3 is chosen.
        elif playerChoice == 3:
            print('\nGoodbye!')
            time.sleep(2)
            break
        
        #Input validation, if the player picks an option that is not valid, asks to see the menu again and if y, the while loop resets back to the top and displays the menu.
        else:
            playAgain = str(input('\nSorry, that is not an option, would you like to see the menu again (y/n)? '))
main()