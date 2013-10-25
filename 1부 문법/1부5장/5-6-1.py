# -*- coding: cp949 -*-
class CounterManager:
    insCount = 0
    def __init__(self):         # 인스턴스 객체가 생성시 클래스 영역의 insCount 변수 증가 
        CounterManager.insCount += 1
    def printInstaceCount():    # 인스턴스 객체 갯수 출력 
        print ("Instance Count: ", CounterManager.insCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.printInstaceCount()        # 인스턴스 개수 출력 
b.printInstaceCount()           # 암시적으로 인스턴스 객체를 받기 때문에 Error가 발생
