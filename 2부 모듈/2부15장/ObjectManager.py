# -*- coding: cp949 -*-
import weakref
class ObjectManager:
    def __init__(self):
        self.weakDict = weakref.WeakValueDictionary()

    def InputObject(self, obj):
        objectID = id(obj)                # 입력받은 객체의 ID 생성
        self.weakDict[objectID] = obj     # 약한 딕셔너리의 값으로 입력 
        return objectID

    def GetObject(self, objectID):
        try:
            return self.weakDict[objectID]    # 객체가 존재하는 경우 반환
        except:
            return None                       # 객체가 소멸된 경우 None 반환
