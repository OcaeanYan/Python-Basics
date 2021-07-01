# -*- coding: utf-8 -*-

# 在一个list中，删掉偶数，只保留奇数
def is_odd(d):
    return d % 2 == 1


# 一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


# 用filter求素数,计算素数的一个方法是埃氏筛法
# 1.先构造一个从3开始的奇数序列,注意这是一个生成器，并且是一个无限序列
def _odd_iter():
    x = 1
    while True:
        x = x + 2
        yield x


# 2.定义一个筛选函数
def _not_divisible(s):
    return lambda x: x % s > 0


# 3.定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        x = next(it)  # 返回序列的第一个数
        yield x
        it = filter(_not_divisible(x), it)  # 构造新序列


# 练习题：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    if isinstance(n, int):  # 判断是否为整数型
        listTmp = list(str(n))
        if len(listTmp) >= 2:  # 整数长度大于等于2的，即10以上的整数
            l = int(len(listTmp) / 2)   # 根据长度分为 前半部分和后半部分
            s1 = listTmp[:l]    # 前半部分
            if len(listTmp) % 2 == 0:
                s2 = listTmp[l:]    # 后半部分
            else:
                s2 = listTmp[l + 1:]
            s2.reverse()    # 将后半部分反转序列，进行比对
            return s1 == s2
        elif len(listTmp) == 1:
            return True


if __name__ == '__main__':
    # # 在一个list中，删掉偶数，只保留奇数
    # a = list(filter(is_odd, [1, 2, 4, 7, 3, 10, 15]))
    # print(a)
    #
    # # 一个序列中的空字符串删掉
    # b = list(filter(not_empty, ['A', '', 'B', None, 'C ', '  ']))
    # print(b)
    #
    # # 用filter求素数,计算素数的一个方法是埃氏筛法
    # # 4.由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
    # for i in primes():
    #     if i < 1000:
    #         print(i)
    #     else:
    #         break

    # 练习题：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
    # 测试:
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')
