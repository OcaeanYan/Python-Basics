# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types


def fn():
    pass


class MyDog(object):
    def __len__(self):
        return 100


# 把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


def readData(fp):
    pass


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


if __name__ == '__main__':
    # a = type(123)
    # b = type('str')
    # c = type(None)
    # d = type([1, 2])
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    # 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
    # print(type(fn) == types.FunctionType)
    # print(type(abs) == types.BuiltinFunctionType)
    # print(type(lambda x: x) == types.LambdaType)
    # print(type((x for x in range(10))) == types.GeneratorType)

    # 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
    # 比如，获得一个str对象的所有属性和方法：
    # a = dir('ABC')
    # print(a)
    # b = len('ABC')
    # print(b)
    # c = 'ABC'.__len__()
    # print(c)

    # dog = MyDog()
    # len(dog)

    # 把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
    obj = MyObject()
    # a = hasattr(obj, 'x') # 有属性'x'吗？
    # b = obj.x
    # c = hasattr(obj, 'y') # 有属性'y'吗？
    # d = setattr(obj, 'y', 19) # 设置一个属性'y'
    # e = hasattr(obj, 'y') # 有属性'y'吗？
    # f = getattr(obj, 'y') # 获取属性'y'
    # g = obj.y  # 获取属性'y'
    # h = getattr(obj, 'z', 404)
    # print(a, '\n', b, '\n', c, '\n', d, '\n', e, '\n', f, \n, g)
    # print(h)

    a = hasattr(obj, 'power')  # 有属性'power'吗？
    b = getattr(obj, 'power')  # 获取属性'power'
    c = fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
    d = fn  # fn指向obj.power
    e = fn()  # 调用fn()与调用obj.power()是一样的
    print(a, '\n', b, '\n', c, '\n', d, '\n', e)

    sum = obj.x + obj.y
    # 不要这样写了
    # sum = getattr(obj, 'x') + getattr(obj, 'y')
