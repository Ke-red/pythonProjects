#
#   Derek Clarke
#   Restaurant Bill Generator
#

def main():
    #Ask for costs, store as variables
    print('Restaurant Bill Generator ...\n')
    
    food = float(input("Please enter cost of food:"))
    drink = float(input("   \"  \"  Cost of drinks:"))
    print ()

    #Do a little bit of math on our variables
    meal = float(food+drink)
    tax = 0.075
    tip = 0.18
    taxamount = meal * tax
    tipamount = meal * tip
    total = meal + taxamount + tipamount

    # Print total bill
    print(f'Restaurant Bill\n-------------------------------\n')
    print(f'Cost of Meal:\t$ {meal:10.2f}') 
    print(f'Tax Amount:\t$ {taxamount:10.2f}')
    print(f'Tip Amount:\t$ {tipamount:10.2f}')
    print(f'\t\t---------------\n')
    print(f'Total:\t\t$ {total:10.2f}')
main()