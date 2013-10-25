# -*- coding: cp949 -*-
class Sequencer:
    def __init__(self, maxValue):       # 생성자 메소드
        self.maxValue = maxValue
    def __len__(self):                  # len()호출시
        return self.maxValue
    def __getitem__(self, index):      # 인덱스로 아이템의 값을 접근 
        if( 0 < index <= self.maxValue):
            return index*10
        else:
            raise IndexError("Index out of range")
    def __contains__(self, item):       # 불린 형태로 인덱스를 넘어갔는지 반환 
        return (0 < item <= self.maxValue)
