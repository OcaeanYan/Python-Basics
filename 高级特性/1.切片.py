# -*- coding: utf-8 -*-


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[0:-1]
    return  s

if __name__ == '__main__':

# 练习题:利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()
    if trim('hello  ') != 'hello':
        print('测试失败1!')
    elif trim('  hello') != 'hello':
        print('测试失败2!')
    elif trim('  hello  ') != 'hello':
        print('测试失败3!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败4!')
    elif trim('') != '':
        print('测试失败5!')
    elif trim('    ') != '':
        print('测试失败6!')
    else:
        print('测试成功7!')

# 1.构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现
    # L = []
    # n = 1
    # while n <= 99:
    #    L.append(n)
    #    n = n + 2
    # print(L)

# 2.切片

    # 2.1 循环取前三位
    # L = ['James', 'Kobe', 'Jordan', 'Melo', 'Paul']
    # r = []
    # n = 3
    # for i in range(n):
    #     r.append(L[i])
    # print(r)

    # 2.2 切片取前三位
    # L = ['James', 'Kobe', 'Jordan', 'Melo', 'Paul']
    # print(L[0:3])
    # print(L[:3])
    # print(L[1:3])
    # print(L[-2:])
    # print(L[-2:-1])
    # print(L[-1:])
    # print(L[::-1]) # 倒序输出

    # 2.3 切片取数列
    # L = list(range(100))
    # print(L)
    # print(L[:10])
    # print(L[-10:])
    # print(L[10:20])
    # print(L[:10:2])
    # print(L[::5])
    # print(L[::-1])

    # 2.4 tuple切片
    # a = (0, 1, 2, 3, 4, 5)
    # print(a[:3])
    # print(a[:1])
    # print(a[1:])
    # print(a[0:-1])

    # 2.5 字符串切片
    # a = 'ABCDEFGH'
    # print(a[:3])
    # print(a[::2])


