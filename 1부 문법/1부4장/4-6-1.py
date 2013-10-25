# -*- coding: cp949 -*-
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
    if i % 2 == 0:   
        continue
    print("Item: {0}".format(i))
else:
    print("Exit without break.")      # break으로 루프가 종료되지 않은 경우 출력됩니다.
print("Always this is printed")       # 루프 외부 문장
