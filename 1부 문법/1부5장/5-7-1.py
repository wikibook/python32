# -*- coding: cp949 -*-
class GString:
    def __init__(self, init = None):    
        self.content = init
    def __sub__(self, str):             # '-'연산자를 중복 
        for i in str:
            self.content = self.content.replace(i, '')
        return GString(self.content)

    def __abs__(self):                  # 'abs()' 내장 함수를 중복 
        return GString(self.content.upper())

    def Print(self):
        print (self.content);

g = GString("aBcdef")
g -= "df"           # '-'연산자가 중복된 경우 '-='도 지원 
g.Print()           # 출력 결과: aBce
g = abs(g)
g.Print()           # 출력 결과: ABCE 
