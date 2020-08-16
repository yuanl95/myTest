# -*- ecoding: utf-8 -*-
# @Author: yunaL

import time
from operator import itemgetter

# 自定义异常类
class MyException(Exception):
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason

def checkInputType(left,right):
    '''
    检查输入的参数是否为int类型
    '''
    if not type(left)==int:
        raise MyException("TypeException", "left为非预期的输入类型")
    if not type(right)==int:
        raise MyException("TypeException", "right为非预期的输入类型")

def checkArray(array,name,isPrint=True):
    '''
    校验排序后结果是否为递增序列
    '''
    length=len(array)
    flag=True
    for i in range(1,length):
        if array[i-1]>array[i]:
            flag=False
            break
    if isPrint:
        if(flag):
            return name+'递增排序正确'
        else:
            return name+'排序错误'
    else:
        return flag

def costTime(data,f,isPrintData=False):
    '''
    查询单个排序算法的计时函数
    '''
    if isPrintData:
        print('初始输入的数据',data)
    start = time.clock()
    f(data, 0, len(data) - 1)
    elapsed = (time.clock() - start)
    print(f.__name__,"函数的排序用时为:", elapsed,checkArray(data,f.__name__))
    if isPrintData:
        print('进排序后的数据',data)

def costTimeList(data,listF):
    '''
    查询多个排序算法的计时函数
    '''
    result=[]
    for f in listF:
        start = time.clock()
        d=data.copy()
        f(d, 0, len(data) - 1)
        elapsed = (time.clock() - start)
        if checkArray(d,f.__name__,isPrint=False):
            result.append((f.__name__, elapsed))
    print('按照使用时间长短排序的结果为:',sorted(result,key=itemgetter(1,0)))
