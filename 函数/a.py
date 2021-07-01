import math

def quadratic(a,b,c):
    d = b*b-4*a*c
    if d >= 0:
        x = (-b+math.sqrt(d))/(2*a)
        y = (-b-math.sqrt(d))/(2*a)
        return x, y
    else:
        return 'no answer!'

if __name__ == '__main__':
    a=quadratic(2, 3, 1)
    b=quadratic(1, 3, -4)
    print('quadratic(2,3,1) =', a)
    print('quadratic(1,3,4) =', b)

    if a != (-0.5, -1.0):
        print('测试失败')
    elif b != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')