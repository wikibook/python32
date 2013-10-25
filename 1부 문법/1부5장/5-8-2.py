# -*- coding: cp949 -*-
class Person:
    " 부모 클래스 "
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber

    def PrintInfo(self):    
        print ("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

    def PrintPersonData(self):
        print ("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Student(Person):
    " 자식 클래스 "
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)    # 명시적으로 Person 생성자를 호출
        self.Subject = subject
        self.StudentID = studentID
