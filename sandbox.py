def main():
    inFile = open(file, 'r')
    course = inFile.readline()
    professor = inFile.readline()
    professor = professor.rstrip('\n')
    term = inFile.readline()
    print ('Professor:', professor, '\t\tTerm:', term)
    print ("{0:<20s} {1:^10}".format("Student Name", "Grade"))
    print ("-"*30)
    student = inFile.readline()
    while student != '':
        #Read Grade for each student
        grade = inFile.readline()
        #Strip new lines
        student = student.rstrip('\n')   
        #Convert numerical values
        grade = eval(grade)    
        #Display student and grade
        print ("{0:<20s} {1:^10}".format(student, grade))
        #read next student
        student = inFile.readline()
main()