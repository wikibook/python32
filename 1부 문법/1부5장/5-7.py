# -*- coding: cp949 -*-
class GString:
    def __init__(self, init = None):    # 생성자 
        self.content = init

    def __sub__(self, str):             # '-' 연산자 중복 
        for i in str:
            self.content = self.content.replace(i, '')
        return GString(self.content)

    def Remove(self, str):              # Remove 메소드는 '-' 연산자 중복과 동일하기에 '__sub__'를 재호출
        return self.__sub__(str)
