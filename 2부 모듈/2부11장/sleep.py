# -*- coding: cp949 -*-
import time
t = time.time()
time.sleep(10)		# 10 초간 sleep
t2 = time.time()

spendtime = t2 - t
print("Before timestemp: ", t)
print("After timestemp: ", t2)
print("Wait {0} seconds".format(spendtime))
