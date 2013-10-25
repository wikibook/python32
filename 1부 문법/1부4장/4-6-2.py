# -*- coding: cp949 -*-
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
    if i > 5:                       # i가 5보다 큰 경우, 순회 중인 루프가 break으로 종료됩니다.
        break
    print("Item: {0}".format(i))
else:
    print("Exit without break.")    # break로 루프가 종료되기 때문에, 출력되지 않습니다.
print("Always this is printed")
