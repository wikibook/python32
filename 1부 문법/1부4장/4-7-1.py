# -*- coding: cp949 -*-
import time
l = range(1000)

t = time.mktime(time.localtime())      # for문으로 각 인자를 출력하는 경우
for i in l:
    print (i,)
t1 = time.mktime(time.localtime()) - t

t = time.mktime(time.localtime())      # join() 메소드를 이용하여 출력하는 경우
print (", ".join(str(i) for i in l))
t2 = time.mktime(time.localtime()) - t

print ("for 문으로 각 인자를 출력")          # 측정한 시간 출력 
print ("Take {0} seconds".format(t1))
print ("join() 메소드로 출력")
print ("Take {0} seconds".format(t2))
