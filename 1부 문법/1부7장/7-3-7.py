# -*- coding: cp949 -*-
FilePath = './test.txt'

try:
    f = open(FilePath, 'r')
    try:
        data = f.read(128)
        print(data)
    finally:
        f.close() 
except IOError:
    print("Fail to open {0} file".format(FilePath))
