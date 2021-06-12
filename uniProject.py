class Student:
    def __init__(self, name, age, major, number):
        self.name = name
        self.age = age
        self.major = major
        self.number = number

    def getName(self):
        return(self.name)

    def getAge(self):
        return(self.age)

    def getMajor(self):
        return(self.major)

    def getNumber(self):
        return(self.number)

    def changeNumber(self, inputedValue):
        self.number = inputedValue

    def changeName(self, inputedValue):
        self.name = inputedValue

    def changeAge(self, inputedValue):
        self.age = inputedValue

    def changeMajor(self, inputedValue):
        self.major = inputedValue

    def changeNumber(self, inputedValue):
        self.number = inputedValue

    def getAllDetails(self):
        return f"name: {self.name}, age: {self.age}, major: {self.major}, number: {self.number}"

studentList = []

#* functions *#
def helperFn():
    print("""
            >type 'help' or '-h' for help.
            >type 'addStudent' or '-add' to add a new student.
            >type 'getStudents' or '-getAll' to get all of the students.
            >type 'getStudentByNumber' or '-getByNum' to find e specific.
            >type 'exportAll' or '-xAll' to export all the data to a text file.
            >type 'queit' or 'exit' to exit.
        """)

def addStudent():
    name = input('student name: ')
    age = input('student age: ')
    major = input('student major: ')
    number = input('student number: ')

    student = Student(name, age, major, number)

    studentList.append(student)
    print(f'{name} has been added to students! \n')

def getStudentsList():
    for student in studentList:
        print(student.getAllDetails())
    print('\n')

def getStudentByNumber():
    foundedStudent = ''

    inputNumber = input('your student number: ')

    for student in studentList:
        if str(student.getNumber()) == str(inputNumber):
            foundedStudent = student

    if foundedStudent == '':
        print('student by this number does not exist \n')
        return #exits the function
    
    def helperFn():
        print("""
            -type 'help' or '-h' for help.
            -type 'changeName' or '-cName' to change the name.
            -type 'changeAge' or '-cAge' to change the name.
            -type 'changeMajor' or '-cMajor' to change the name.
            -type 'changeNumber' or '-cNumber' to change the name.
            -type 'queit' or 'exit' to exit.
        """)

    def changeName():
        newValue = input('what is the new name?: ')
        foundedStudent.changeName(newValue)
        print(f'name has been successfully changed to {newValue}\n')

    def changeAge():
        newValue = input('what is the new age?: ')
        foundedStudent.changeAge(newValue)
        print(f'age has been successfully changed to {newValue}\n')
        
    def changeMajor():
        newValue = input('what is the new major?: ')
        foundedStudent.changeMajor(newValue)
        print(f'major has been successfully changed to {newValue}\n')

    def changeNumber():
        newValue = input('what is the new number?: ')
        foundedStudent.changeNumber(newValue)
        print(f'number has been successfully changed to {newValue}\n')

  #* Switch Keys *#  
    switchKeys = { 
        'help': helperFn, # getting help #
        '-h': helperFn,
        'changeName': changeName,
        '-cName' : changeName,
        'changeAge': changeAge,
        '-cAge' : changeAge,
        'changeMajor': changeMajor,
        '-cMajor' : changeMajor,
        'changeNumber': changeNumber,
        '-cNumber' : changeNumber,
    }

    #* defining Switch function *#
    print(f'there was {foundedStudent.getName()} by that number!\n')

    #* Infinte Loop *#
    def switch(function):
        return switchKeys.get(function, lambda: print('This function does not exist, type -h for help!\n'))()

    while True:
        userInput = input('what you want to do with it (type -h for help)? ');

        if userInput == 'exit':
            print('\n')
            break

        if userInput == 'removeFromList' or userInput == '-remove':
            studentList.remove(inputNumber)
            print('student has been removed from list\n')
            break

        switch(userInput)

def exportToTextFile():
    textFileContent = 'name\t age\t major\t number\n'
    for student in studentList:
        textFileContent = textFileContent + f'{student.getName()}\t {student.getAge()}\t {student.getMajor()}\t {student.getNumber()}\n'

    with open('export.txt', 'w') as f:
        f.write(textFileContent)

    print('exported all the data to a textfile! \n\n')

#* Switch Keys *#
switchKeys = { 
    'help': helperFn, # getting help #
    '-h': helperFn,
    'addStudent' : addStudent, # adding student #
    '-add' : addStudent,
    'getStudents': getStudentsList, # getting all students #
    '-getAll': getStudentsList,
    'getStudentByNumber': getStudentByNumber, # getting specific student #
    '-getByNum': getStudentByNumber,
    'exportAll': exportToTextFile, # export all the files to a text file #
    '-exAll': exportToTextFile,
}

#* defining Switch function *#
def switch(function):
    return switchKeys.get(function, lambda: print('This function does not exist!'))()


#* Infinte Loop *#
while True:
    userInput = input('Enter your request (type -h or help for help): ')

    if userInput == 'exit':
        break

    switch(userInput)