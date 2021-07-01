# -*- coding: utf-8 -*-

# 把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

    # 联系题 用匿名函数改造下面的代码
    # 原：def is_odd(n):
    #     return n % 2 == 1
    #
    # L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda n : n % 2 == 1, range(1, 20)))

if __name__ == '__main__':
    # 关键字lambda表示匿名函数，冒号前面的x表示函数参数
    a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(a)

    f = lambda x: x * x
    print(f)
    print(f(5))

    # 把匿名函数作为返回值返回
    print(build(1, 2))

    # 联系题 用匿名函数改造下面的代码
    # 原：def is_odd(n):
    #     return n % 2 == 1
    #
    # L = list(filter(is_odd, range(1, 20)))
    L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
    print(L)
