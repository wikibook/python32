# -*- coding: cp949 -*-
str = "NOT Class Member" # 전역 변수
class GString:
    str = ""             # 클래스 객체 멤버 변수
    def Set(self, msg):
        self.str = msg
    def Print(self):  
        print(str)       # self를 이용하여 Class 멤버를 접근하지 않는 경우 
                         # 이름이 동일한 전역 변수에 접근하여 출력

g = GString()
g.Set("First Message")
g.Print()
