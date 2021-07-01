# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # 关键字lambda表示匿名函数，冒号前面的x表示函数参数
    a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(a)

    f = lambda x: x * x
    print(f)
    print(f(5))
