#
#   Derek Clarke
#   gradesSummary.py
#
#   Input: Ask user what file they would like to open, throw error if file is not found
#   Processing: Take the course name, professor, and the term from the first three lines and hold in variable for later printing, 
#   then process every student name and grade in the file, stripping the line for each student so the grade is on the same line,
#   counting every grade that is greater than or equal to 60 and add 1 to the passing varibale, else marking them as a fail. Print
#   formatted table, once the while loop reaches a blank line, calculate the total number of students from the failed and passed variables, 
#   then divide the total from the sum of the grades to get an average and the amount of passing students to get a percentage of students who passed.
#   Output: Print a formatted output with all of the students' names, and their grades in two columns called Student Name and Grades, 
#   then, printing the total amount of failed and passing studnets, then printing the percentage of those passer and the average grade


def main ():
    #Control variable
    runReport = 'y'
    while runReport == 'y':
        print ('Course Grades Summary Report ...')
        file = input('Enter name of course file:')
        print()
        displayFile(file)
        runReport = input('Would you like to process another file? (y/n)')

#Function to open and format file for output to python
def displayFile(file):        
    try:
        #Open file from input
        inFile = open(file, 'r')
        print ('-'*50)
        print ('\tBroward College Grades Summary')
        print ('-'*50)
        print()
        course = inFile.readline()
        professor = inFile.readline()
        professor = professor.rstrip('\n')
        term = inFile.readline()
        print (course)
        print ('Professor:', professor, '\t\tTerm:', term)
        #Format output to two "columns"
        print ("{0:<20s} {1:^10}".format("Student Name", "Grade"))
        print ("-"*30)
        #Student performance
        passed = 0
        failed = 0
        sum = 0
        student = inFile.readline()
        while student != '':
            #Read Grade for each student
            grade = inFile.readline()
            #Strip new lines
            student = student.rstrip('\n')   
            #Convert numerical values
            grade = eval(grade)
            if grade >= 60:
                passed += 1
            else:
                failed += 1    
            #Display student and grade
            print ("{0:<20s} {1:^10}".format(student, grade))
            #Calculate the sum of everyone's grades
            sum += grade
            #Read next student
            student = inFile.readline()
        totalstudents = failed + passed
        print ('Students\' Performance')
        print ('-'*30)
        print ('Passed:', passed, 'Failed:', failed)
        #Calculate the percentage of students who passed
        print (f'Passing Percent: {passed / totalstudents * 100:.0f}')
        #Calculate the average grade of all studnets
        print (f'Average Grade: {sum // totalstudents}')
        inFile.close()
    #Input validation, if program cannot find file name, print error and end function, asking user if they'd like to process another file        
    except FileNotFoundError:
        print('Error ... ', file, 'file not found.')
main()