#   Derek Clarke
#   weight.py
#
#   Prompt user whether they would like to display the guideline or use the weight table, when using option 2 trigger the following IPO:
#   
#   Input: When selecting option 2, ask for weight
#
#   Process:
#   1. Take weight input
#   2. Subtract 4lbs. from the original weight over 6 months
#   3. Display table of weight loss over the next 6 months
#
#   Output: Weight loss over 6 months
#
#


def main() :
    #   Display title of program and ask user which option they would like
    print('500 Less a Day Makes the Weight Go Away ...')

    print('Choose one of the following options: \n \t 1. Display "10 ways to cut 500 calories" guideline. \n \t 2. Generate next semester expected weight table. \n \t 3. Quit')
    option = int(input('Option:'))

    #   If the option input is less than 1 or greater than 3, prompt user with error and ask for new input
    if option <1 or option >3 :
        print('Error ... Invalid option. Try Again\n')
        option = int(input('Option:'))

    #   If the option picked is 1, print this output
    if option == 1:
        print('Try these 10 ways to cut 500 calories every day\n \t', 
            '* Swap your snack.\n \t',
            '* Cut one high-calorie treat.\n \t',
            '* DO NOT drink your calories.\n \t',
            '* Make low calorie substitutions.\n \t',
            '* Ask for a doggie bag.\n \t',
            '* Just say \"No\" to fried food.\n \t',
            '* Build a thinner pizza.\n \t',
            '* Use a smaller plate\n \t', 
            '* Avoid alcohol.\n',
            'Source: US National Library of Medicine')
        
    #   If the option picked is 2, prompt for starting weight and print an output table with the expected weight loss per month for 6 months      
    if option == 2:
        weight = int(input('Please enter starting weight in pounds (>=100): '))
        while weight < 100:
            print('Error ... Invalid weight. Try Again')
            weight = int(input('Please enter starting weight in pounds (>=100): '))
        print('--------------')
        print('Month\tWeight')
        print('--------------')
        month = 1
        while month != 7:
            weight -= 4
            print(month,'\t', weight,'lb.' )
            month += 1
    
    #   If the option picked is 3, tell user good byr and terminate
    if option == 3:
        print ('Good Bye ...')
main ()