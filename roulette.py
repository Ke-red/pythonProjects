##      Roulette Wheel
#
##      Derek Clarke

#Print name of app and ask for user input of an integer between 0 - 36

def main ():
    print('Roulette Wheel Colors App ...')
    pocket = int(input('Please enter pocket number (0-36):'))
    
#Define range of acceptable numbers (0-36), and check against each set of numbers to find out if the even number
#is red or black and if true, prints the color or asks the user to try again if the number falls out of scope

    if pocket >= 0 and pocket <= 36:

        if pocket == 0: 
            pocket = "green"
    
        elif pocket >= 1 and pocket <= 10:
            if pocket % 2 == 0: pocket = "black"
            else: pocket = "red"
    
        elif pocket >= 11 and pocket <= 18:
            if pocket % 2 == 0: pocket = "red"
            else: pocket = "black"

        elif pocket >= 19 and pocket <= 28:
            if pocket % 2 == 0: pocket = "black"
            else: pocket = "red"
        
        elif pocket >= 29 and pocket <= 36:
            if pocket % 2 == 0: pocket = "red"
            else: pocket = "black"

        print('The color of the wheel pocket is', pocket)

    else: print("Error ... Invalid pocket. Try Again")
main()