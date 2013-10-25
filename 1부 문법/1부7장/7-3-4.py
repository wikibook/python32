# -*- coding: cp949 -*-
def devide(a, b):
    return a/b
try:
    c = devide(5, "af")
except TypeError as e:	# 전달되는 예외 인스턴스 객체를 e로 받아서 사용
    print('에러: ', e.args[0])
except Exception:
	print('음~ 무슨 에러인지 모르겠어요!!')
