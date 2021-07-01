# -*- coding: utf-8 -*-

# 基础的高阶函数
# def add(x, y, f):
#     return f(x) + f(y)

#  Python内建了map()和reduce()函数

# def f(x):
#     return x * x

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 效果：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

# def add(x, y):
#     return x + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

# 用lambda函数进一步简化成.lambda函数是简化函数定义
# def char2num(s):
#     return DIGITS[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


# sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce


def prod(L):
    def m(x, y):
        return x * y

    return reduce(m, L)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    n = s.index('.')
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


if __name__ == '__main__':
    # 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
    #  输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
    # 测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    #   sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    # 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

    # 基础高阶函数
    # print(add(-5, 6, abs))

    # Python内建了map()和reduce()函数
    # r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    # print(list(r))

    # map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    # s = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # print(s)

    # reduce的用法
    # print(reduce(add, [1, 3, 5, 7, 9]))

    # print(str2int('13579'))
