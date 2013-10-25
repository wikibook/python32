# -*- coding: cp949 -*-
class MyClass:
    def __init__(self, value):  # 생성자 메소드
        self.Value = value
        print("Class is created! Value = ", value)
        
    def __del__(self):          # 소멸자 메소드
        print("Class is deleted!")

def foo():  
    d = MyClass(10)      # 함수 foo 블록안에서만 인스턴스 객체 d가 존재

foo() 
