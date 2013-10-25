# -*- coding: cp949 -*-
class NegativeDivisionError(Exception):   # 사용자 정의 예외 정의
    def __init__(self, value):
        self.value = value

def PositiveDevide(a, b):
    if(b < 0):         # 제수가 0보다 작은 경우, NegativeDivisionError 발생
        raise NegativeDivisionError(b)
    return a/b


try:
    ret = PositiveDevide(10, -3)
    print('10 / 3 = {0}'.format(ret))
except NegativeDivisionError as e:     # 사용자 정의 예외인 경우
    print('Error - Second argument of PositiveDevide is ', e.value)
except ZeroDivisionError as e:         # '0'으로 나누는 경우
    print('Error - ', e.args[0])
except :         # 그 외 모든 예외의 경우
    print(e.args)
