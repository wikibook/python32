# -*- coding: cp949 -*-
class CounterManager:
    __insCount = 0			# 이름 변경을 위하여 '__'를 변수명 앞에 사용 
    def __init__(self):    
        CounterManager.__insCount += 1
    def staticPrintCount():
        print ("Instance Count: %d" % CounterManager.__insCount)  # 클래스 내부에서 사용시 선언한 이름과 동일하게 사용 가능
    SPrintCount = staticmethod(staticPrintCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.SPrintCount()
