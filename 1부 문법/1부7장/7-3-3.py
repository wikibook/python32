# -*- coding: cp949 -*-
def devide(a, b):
    return a/b

try:
    c = devide(5, 2)
except ZeroDivisionError:
    print('두번째 인자는 0이면 안됩니다.')
except TypeError:
    print('모든 인수는 숫자이여야 합니다.')
except:
    print('ZeroDivisionError, TypeError를 제외한 다른 에러')
else:      # 예외가 발생하지 않는 경우
    print('Result: {0}'.format(c))
finally:   # 예외 발생 유무와 상관없이 수행 
    print('항상 finally 블록은 수행됩니다.')
