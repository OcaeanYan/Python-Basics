# -*- coding: utf-8 -*-

def mul(*num):
    if len(num) == 0:
        raise TypeError
    else:
        res=1
        for x in num:
            res = res * x
        return res

if __name__ == '__main__':
    print('mul(5) =', mul(5))
    print('mul(5, 6) =', mul(5, 6))
    print('mul(5, 6, 7) =', mul(5, 6, 7))
    print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
    if mul(5) != 5:
        print('测试失败1!')
    elif mul(5, 6) != 30:
        print('测试失败2!')
    elif mul(5, 6, 7) != 210:
        print('测试失败3!')
    elif mul(5, 6, 7, 9) != 1890:
        print('测试失败4!')
    else:
        try:
            mul()
            print('测试失败5!')
        except TypeError:
            print('测试成功6!')