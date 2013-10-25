# -*- coding: cp949 -*-
class CounterManager:
    insCount = 0
    def __init__(self):    
        CounterManager.insCount += 1
    def staticPrintCount():                         # 정적 메소드 정의
        print ("Instance Count: ", CounterManager.insCount)
    SPrintCount = staticmethod(staticPrintCount)    # 정적 메소드로 등록 

    def classPrintCount(cls):                       # 클래스 메소드 정의(암시적으로 첫 인자는 클래스를 받음) 
        print ("Instance Count: ", cls.insCount)
    CPrintCount = classmethod(classPrintCount)      # 클래스 메소드로 등록 

a, b, c = CounterManager(), CounterManager(), CounterManager()

# 정적 메소드로 인스턴스 객체 갯수를 출력 
CounterManager.SPrintCount()       
b.SPrintCount()

# 클래스 메소드로 인스턴스 객체 갯수를 출력
CounterManager.CPrintCount()
b.CPrintCount()
