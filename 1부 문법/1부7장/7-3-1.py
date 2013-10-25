# -*- coding: cp949 -*-
def devide(a, b):
	return a/b

try:
	c = devide(5, 'string')
except ZeroDivisionError:
	print('두번째 인자는 0이면 안됩니다.')
except TypeError:
	print('모든 인수는 숫자이어야 합니다.')
except:
	print('음~ 무슨 에러인지 모르겠어요!!')  
