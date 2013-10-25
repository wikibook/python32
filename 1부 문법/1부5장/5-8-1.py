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
	def __init__(self, name, phoneNumber, subject, studentID):   # 자식 클래스의 생성자 메소드
		self.Name = name
		self.PhoneNumber = phoneNumber
		self.Subject = subject
		self.StudentID = studentID
