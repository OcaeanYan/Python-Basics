# -*- coding: utf-8 -*-

#   如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b =0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')
    return 'done'

#   在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)

#   杨辉三角
def triangles():

    n = 0
    L = [1]
    while True:
        yield L
        L = [L[i] + L[i + 1 ] for i in range(len(L) - 1 ) ]     # 先生成除首位的数字
        L.insert(0, 1)          # list开头添加 1
        L.append(1)             # list结尾添加 1
        n = n + 1
        print(L)

if __name__ == '__main__':

#   练习题：杨辉三角定义如下，把每一行看做一个list，试写一个generator，不断输出下一行的list：
    # 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')

#   在Python中，这种一边循环一边计算的机制，称为生成器：generator
#     L = [x * x for x in range(10)]
#     print(L)
#
#     g = (x * x for x in range(10))
#     # print(g)
#     for i in g:
#         print(i)

    # f = fib(6)
    # for i in fib(6):
    #     print(i)

    # o = odd()
    # for n in o:
    #     print(n)

#   想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
#     g = fib(6)
#     while True:
#         try:
#             x = next(g)
#             print('g:', x)
#         except StopIteration as e:
#             print('Generator return value:', e.value)
#             break
