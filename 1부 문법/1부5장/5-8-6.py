# -*- coding: cp949 -*-
class Tiger:
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")

class Lion:
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")

class Liger(Tiger, Lion):	# 상속받을 클래스들
    def Play(self):
        print("라이거만의 사육사와 재미있게 놀기")
