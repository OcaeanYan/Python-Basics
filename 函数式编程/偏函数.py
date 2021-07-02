# functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
import functools
# 要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base = 2):
    return int(x, base)

def main2():
    max2=functools.partial(max,100)
    result=max(1,2,4,7,99)
    result1=max(1,2,3,102)
    print((result,result1))

if __name__ == '__main__':
    # int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
    a = int('12345')
    print(a)

    # int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
    b = int('12345', base=8)
    print(b)

    c = int('12345', 16)
    print(c)

    # 定义一个int2()的函数，默认把base=2传进去
    d = int2('1000000')
    e = int2('1010101')
    print('This is d=', d, '\nThis is e=', e)

    # functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
    int2 = functools.partial(int, base=2)
    a1 = int2('1000000')
    a2 = int2('1010101')
    print('This is a1=', a1, '\nThis is a2=', a2)

    main2()