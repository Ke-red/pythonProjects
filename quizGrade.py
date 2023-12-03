#   quizGrade.py
#
#   Derek Clarke
#
#   Input: Ask user for the student's name and file with their answers for quiz
#
#   Process: Take file provided, convert the file to a list and compare it against
#   a list of correct answers, stating how many questions the student got right
#   or wrong and which answers they got wrong.
#
#   Output: Print the result, and ask whether the user would like to process 
#   another file. 
#

#Answer key and passing grade to determine correct/incorrect answers and whether student passes or fails
quizAnswers = ['A', 'C', 'A', 'B', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'D', 'D', 'B']
passing = 11

#Ask for student name and the file they would like to proccess, then when functions are complete, ask if user would like to proces another file
def main():
    again = 'y'
    while again == 'y':
        print('Quiz Grading App ...')
        name = str(input('Student Name:'))
        file = str(input('Student answers file:'))
        studentAnswers = convertFile(file)
        checkFile(studentAnswers, name)
        again = input('Would you like to process another quiz (y/n)?')

#Funtion to conver the given file to a list, and return an error if the file cannot be found
def convertFile(file):
    try:
        inFile = open(file, 'r')
        studentAnswers = inFile.read().split("\n")
        inFile.close()
        return studentAnswers
    except FileNotFoundError:
        print(f'Error, could not process {file}')

#Create funtion to take the list created from the convertFile function and compare the list to the quizAnswers list
def checkFile(studentAnswers, name):
    
    #Compare two lists together and create a new list called correct with all of the indexes that match the quizAnswered list
    correct = [i for i, x in enumerate(zip(quizAnswers,studentAnswers), start= 1) if x[0]==x[1]]
   
    #Compare two lists together and create a new list call incorrect with only the indexes that don't match in the quizAnswered lis
    incorrect = [i for i, x in enumerate(zip(quizAnswers,studentAnswers), start= 1) if x[0]!=x[1]]
    incorrect = tuple(incorrect)
   
    #Get lengths of lists for comparison
    questions = len(quizAnswers)
    numberCorrect = len(correct)
    numberIncorrect = len(incorrect)
    
    #Output student name, and their correct and incorrect answers and whether they passed or failed if their score is higher than the passing variable
    print (f'{name} Quiz Results')
    print ('-'* 30)
    print (f'Correct Answers: {numberCorrect}')
    print (f'Incorrect Answers: {numberIncorrect} {incorrect}')
    print ()
    if numberCorrect >= passing:
        print ('Student PASSED the quiz.')
    else:
        print ('Student FAILED the quiz.')    
main()