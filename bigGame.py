#
#
#   Derek Clarke
#   BigGame.py
#   Prompts the user to fill out the pieces to a story
#   and fills it all in at the end
#
def main():
    print('Madlib Game')

    #   User instructions
    print('Enter the following words:')

    #   User prompts and their variables

    PNOUN1 = input("Plural Noun: ")

    FNAME = input("Person's First Name: ")

    NOUN1 = input("Noun: ")

    LNAME = input("Person's Last Name: ")

    PNOUN2 = input("Plural Noun: ")

    PLACE1 = input("Place: ")

    PNOUN3 = input("Plural Noun: ")

    PLACE2 = input("Place: ")

    PNOUN4 = input("Plural Noun: ")

    NOUN2 = input("Noun: ")

    ADJECTIVE1 = input("Adjective: ")

    ADJECTIVE2 = input("Adjective: ")

    VERB = input("Verb: ")

    ADJECTIVE3 = input("Adjective: ")

    #   Tying all the stored variables to the story

    print('The Big Game !!!')
    print()
    print('Hello there, sports',PNOUN1,'!')
    print('This is',FNAME,', talking to you from the press',NOUN1)
    print('in',LNAME,'Stadium, where 57,000 cheering',PNOUN2)
    print('Have gathered to watch (the)',PLACE1, PNOUN3)
    print('take on (the)',PLACE2, PNOUN4,)
    print('Even though the' ,NOUN2, 'is shining, it’s a/an' ,ADJECTIVE1)
    print('cold day with the temperature in the' ,ADJECTIVE2, '20s.')
    print('We’ll be back for the opening',VERB,'-off after a few words')
    print('from our' ,ADJECTIVE3, 'sponsor.')

main()