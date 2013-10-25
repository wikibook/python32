# -*- coding: cp949 -*-
class Animal:
    def __init__(self):
        print("Animal __init__()")

class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self)		# Animal 생성자 메소드 호출
        print("Tiger __init__()")

class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)		# Animal 생성자 메소드 호출
        print("Lion __init__()")

class Liger(Tiger, Lion):
    def __init__(self):
        Tiger.__init__(self)		# Tiger 생성자 메소드 호출
        Lion.__init__(self)			# Lion 생성자 메소드 호출
        print("Liger __init__()")
