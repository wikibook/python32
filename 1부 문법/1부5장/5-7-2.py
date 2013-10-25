# -*- coding: cp949 -*-
class GString:
    def __init__(self, init = None):   
        self.content = init

    def __sub__(self, str):             # '-'연산자 중복
       print("- opreator is called!")

    def __isub__(self, str):            # '-='연산자 중복
        print("-= opreator is called!")

g = GString("aBcdef")
g - "a"     # 출력 결과: - opreator is called!
g -= "a"    # 출력 결과: -= opreator is called!
