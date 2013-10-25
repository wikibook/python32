# -*- coding: cp949 -*-
def RaiseErrorFunc():
    raise NameError("NameError의 인자")

def PropagateError():
    try:
        RaiseErrorFunc()                        
    except:
        print("에러전달 이전에 먼저 이 메세지가 출력됩니다.")
        raise     # 발생한 에러를 상위로 전달 

PropagateError()
