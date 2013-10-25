# -*- coding: cp949 -*-
def RaiseErrorFunc():
    raise NameError     # 내장 예외인 NameError를 발생

try:
    RaiseErrorFunc()
except: 
    print("NameError is Catched")
