# -*- coding: cp949 -*-
def foo(x):
	assert type(x) == int, "Input value must be integer"   # 받은 인자의 type이 정수형인지 검사
	return x*10

ret = foo("a")   # AssertionError가 발생 
print(ret)
