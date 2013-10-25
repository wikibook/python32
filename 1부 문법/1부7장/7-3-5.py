# -*- coding: cp949 -*-
def devide(a, b):
    return a/b
try:
    c = devide(5, 0)
except (ZeroDivisionError, OverflowError, FloatingPointError): # 명시된 에러를 모두 처리 
    print('수치 연산 관련 에러입니다.')
except TypeError:
    print('모든 인수는 숫자이어야 합니다.')
except Exception:
    print('음~ 무슨 에러인지 모르겠어요!!')
