# -*- coding: utf-8 -*-

#   sorted()对上述列表分别按名字排序
def by_name(t):
    return t[0].lower()  # t是tuple，t[0]是姓名（字符串）！！！


#   再按成绩从高到低排序
def by_score(t):
    return t[1]


if __name__ == '__main__':
    # Python内置的sorted()函数就可以对list进行排序：
    a = sorted([36, 5, -12, 10, -21])
    print(a)

    # sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
    b = sorted([36, 6, -12, 9, -21], key=abs)
    print(b)

    # 字符串排序,可实现忽略大小写的排序
    c = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
    print(c)

    # 字符串排序，反向排序，不必改动key函数，可以传入第三个参数reverse=True
    d = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    print(d)

    # 练习题：用一组tuple表示学生名字和成绩，请用sorted()对上述列表分别按名字排序
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key=by_name)
    print(L2)

    L3 = sorted(L, key=by_score, reverse=True)
    print(L3)
