# -*- coding: utf-8 -*-

# 函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum

# 闭包
def count():
    fs = []
    for i in  range(1,4):
        def f():
            return i * i
    return fs

def COUNT():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

# 练习题：利用闭包返回一个计算器函数，每次调用它返回递增整数：
def createCounter():
    n = 0
    def counter():
        nonlocal n  # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
        n += 1
        return n
    return counter



if __name__ == '__main__':
    # 函数作为返回值
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f())
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1() == f2())

    # 闭包
    # 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    # f1, f2, f3 = count()
    f4, f5, f6 = COUNT()
    print(f4())
    print(f5())
    print(f6())

    # 练习题：利用闭包返回一个计算器函数，每次调用它返回递增整数：
    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')