# -*- coding: utf-8 -*-

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        (min, max) = (L[0], L[0])
    for x in L:
        if max < x:
            max = x
        if min > x:
            min = x
    return (min, max)

if __name__ == '__main__':

# 练习题:请使用迭代查找一个list中最小和最大值，并返回一个tuple
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')


    # 1.1 字典dict for循环遍历 key
    # d ={'a': 1,'b': 2,'c': 3}
    # for key in d:
    #     print(key)

    # 1.2 字典dict for循环遍历 value
    # d ={'a': 1,'b': 2,'c': 3}
    # for value in d.values():
    #     print(value)

    # 1.3 字典dict for循环遍历 key和value
    # d = {'a': 1, 'b': 2, 'c': 3}
    # for k,v in d.items():
    #     print(k,v)

    # 如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
    # from collections.abc import Iterable
    # print(isinstance('abc', Iterable))
    # print(isinstance([1, 2, 3], Iterable))
    # print(isinstance(123, Iterable))

    # 要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
    # for i, value in enumerate(['A', 'B', 'C']):
    #     print(i,value)
    # for x,y in [(1,1), (2,3), (3,7)]:
    #     print(x, y)