from functools import *

def intersect (*ar):
    "intersection"
    return reduce(__intersectSC,ar)
 
def __intersectSC(listX,listY):
    setList =[]
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    "difference of sets"
    setList =[]
    intersectSet=intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList


def union(*ar) :
    "union"
    setList = []
    for item in ar:
        for x in item:
            if not x in setList :
                setList.append(x)
    return setList



 




