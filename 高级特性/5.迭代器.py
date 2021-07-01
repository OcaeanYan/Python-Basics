


if __name__ == '__main__':

# 可以使用isinstance()判断一个对象是否是Iterable对象：
    # from collections.abc import Iterable
    # print(isinstance([], Iterable))
    # print(isinstance({}, Iterable))
    # print(isinstance('abc', Iterable))
    # print(isinstance((x for x in range(10)), Iterable))
    # print(isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象
    from collections.abc import Iterator
    print(isinstance((x for x in range(10)), Iterator))
    print(isinstance({}, Iterator))
    print(isinstance([], Iterator))
    print(isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
    print(isinstance(iter([]),Iterator))
    print(isinstance(iter('abc'),Iterator))

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；