# -*- coding: utf-8 -*-




if __name__ == '__main__':
#   如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
#   使用内建的isinstance函数可以判断一个变量是不是字符串
#      x = 'abc'
#      y = 123
#      print(isinstance(x,str))
#      print(isinstance(y,str))
#   练习题：修改列表生成式，通过添加if语句保证列表生成式能正确地执行

    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s,str)]

    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')

    #list 生成式 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # a = list(range(1,11))
    # print(a)

    # #list 生成式 [1x1, 2x2, 3x3, ..., 10x10]
    # L = []
    # for x in range(1,11):
    #     L.append(x * x)
    # print(L)

    # 列表生成式
    # a = [x * x for x in range(1, 11)]
    # print(a)
    #
    # b = [m + n for m in 'ABC' for n in 'XYZ']
    # print(b)

    # 列出当前目录下的所有文件和目录名，可以通过一行代码实现
    # import os   # 导入os模块
    # a = [d for d in os.listdir('.')]     # os.listdir可以列出文件和目录
    # print(a)

    # dict的 items() 可以同时迭代key和value：
    # d = {'x':'A', 'y':'B', 'z':'C'}
    # for k, v in d.items():
    #     print(k, '=', v)

    # e = {'x':'A', 'y':'B', 'z':'C'}
    # f = [k + '=' + v for k, v in e.items()]
    # print(f)

    # list 中所有字符串变为小写：
    # L = ['Hello', 'World', 'CBA', 'AppLE']
    # l = [s.lower()for s in L]
    # print(l)

    # if...else  使用列表生成式. for后面的if是过滤条件，不能带else
    # a = [x for x in range(1, 11) if x % 2 == 0]
    # print(a)

    # for前面的if...else是表达式
    # c = [x if x % 2 == 0 else -x for x in range(1,11)]
    # print(c)