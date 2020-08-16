# -*- ecoding: utf-8 -*-
# @Author: yunaL

import numpy as np

from Utils import *

def quickSort(array,left,right):
    '''
    快速排序，升序排列
    NlogN,不稳定
    '''
    checkInputType(left,right)
    if left>right:
        return
    else:
        #哨兵位
        sb=array[left]
        i,j=left,right
        while(i!=j):
            #升序排列时，要先从右端开始遍历,以避免交换错误
            while(array[j]>=sb and i<j):
                j=j-1
            while (array[i]<=sb and i<j):
                i=i+1
            if(i<j):
                temp=array[j]
                array[j]=array[i]
                array[i]=temp
        #确定当前哨兵位的值在列表中的正确位置，即交换哨兵位和此时i或j位置的值
        array[left]=array[i]
        array[i]=sb
        #使用分治法递归处理前一半和后一半的值
        quickSort(array,left,i-1)
        quickSort(array,i+1,right)

def bubbleSort(temp,left,right):
    '''
    冒泡排序，升序排列
    N^2 稳定
    '''
    checkInputType(left, right)
    if left>right:
        return
    else:
        for i in range(right):
            #每完成一次内循环，便完成一位当前最大值得定位，也因此在下一轮的迭代中减少一次比较。
            for j in range(left,right-i):
                #顺序交换前大后小情况的前后位的值
                if temp[j]>temp[j+1]:
                    a=temp[j]
                    temp[j]=temp[j+1]
                    temp[j+1]=a

def insertSort(array,left,right):
    '''
    插入排序,升序排序，稳定
    N^2
    '''
    checkInputType(left, right)
    if left>right:
        return
    else:
        for i in range(1,right+1):
            current=array[i]
            j=i-1
            while(j>=0):
                if array[j]>current:
                    array[j+1]=array[j]
                    j = j - 1
                else:
                    break
            array[j+1] = current

def selectSort(array,left,right):
    '''
    选择排序，不稳定
    '''
    checkInputType(left, right)
    if left > right:
        return
    else:
        #每次选出当前数组中最小值，并将这个最小值与首位交换顺序
        for i in range(right):
            minValue=array[i]
            minIndex=i
            for j in range(i+1,right+1):
                if(minValue>array[j]):
                    minIndex=j
                    minValue=array[j]
            array[minIndex] = array[i]
            array[i]=minValue



if __name__ == "__main__":
    #随机生成1000个整形一维数组
    test1=np.random.randint(1000,size=1000)
    # test2=test1.copy()
    # test3=test1.copy()
    # test4 = test1.copy()
    # a=[77,88,33,55,99,22,66]
    #排序后改变原数组的单个测试
    # costTime(test1,quickSort)
    # costTime(test2,bubbleSort)
    # costTime(test3,insertSort)
    # costTime(test4,selectSort)
    #排序后不改变原数组的多个排序算法的时间消耗排序
    listF=[quickSort,bubbleSort,insertSort,selectSort]
    costTimeList(test1,listF)



