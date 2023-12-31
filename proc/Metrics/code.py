class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        print(self.name)
    
    def showAge(self):
        print(self.age)

class Student:
    def __init__(self, studentId):
        self.studentId = studentId
    
    def getId(self):
        return self.studentId

class Resident(Person, Student):
    def __init__(self, name, age, id):
        Person._init__(self, name, age)
        Student.__init__(self, id)

resident1 = Resident('John', 30, '102')
resident1.showName()
print(resident1.getID())