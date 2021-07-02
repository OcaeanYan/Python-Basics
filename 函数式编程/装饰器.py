# -*- coding: utf-8 -*-

# decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator

# 能打印日志的decorator
# @log()
# def now():
#     print('2021-07-02')

# 3层嵌套的decorator用法如下
# @log('execute')
# def now():
#     print('2021-07-02')
#

# 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如
import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper


# 针对带参数的decorator
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('call %s():' % func.__name__)
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator


# 练习题：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# import time
# import functools
#
#
# def metric(fn):
#     start = time.time()
#     @functools.wraps(fn)
#     def warpper(*args, **kw):
#         # start = time.time()
#         # 通过time.time()在函数调用前后获取当前时间，差值为耗时
#         # 通过@functools.wraps()将原函数名复制到wrapper()函数中
#         end = time.time() - start
#         print('%s executed in %s ms' % (fn.__name__, end))
#         return fn(*args, **kw)
#     return warpper


# 小结
# 1.请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
# import functools
#
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('begin call %s():' % func.__name__)
#         print('the result of the program is {}'.format(*args, **kw))
#         print('end call %s():' % func.__name__)
#
#     return wrapper
#
#
# @log
# def f2(x, y):
#     return x + y
#
#
# def main():
#     f2(4, 6)
#     print("the name of the function is :" + f2.__name__)

# 2.思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
#     pass
# 又支持：
#
# @log('execute')
# def f():
#     pass
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text != None:
                print('the text is %s and the call %s():' %(text, func.__name__))
                res = func(*args, **kw)
                return res
            else:
                print('call %s ():'%func.__name__)
                res = func(*args, **kw)
                return res
        return wrapper

    if isinstance(text, str):  # 首先如果有参数 就跟原来一样直接返回decorator即可
        return decorator
    else:  # 如果没有参数 其实log(func)就是log里边其实直接传的参数就是func 返回的应该是wrapper
        func = text
        text = None
        return decorator(func)  # 所以这里的应该是直接decorator(func) 返回wrapper

@log("there is a parameter in this edition")
def f1(x,y):
    return x*y

def main1():
    result=f1(2,3)
    print("the result is {}".format(result))
    print("the name of this function(no_parameter) is "+f1.__name__)

@log
def f2(x,y):
    return x+y

def main2():
    result=f2(5,8)
    print("the result of this function(with parameter) is {}".format(result))
    print("the name of this function is "+f2.__name__)

def main():
    number=eval(input("please input a number to decide which the function to run:"))
    if number==1:
        main1()
        print("run successfully!")
    else:
        main2()
        print("Run successfully!")


if __name__ == '__main__':
    # 练习题：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
    # 测试
    # @metric
    # def fast(x, y):
    #     time.sleep(0.0012)
    #     return x + y
    #
    #
    # @metric
    # def slow(x, y, z):
    #     time.sleep(0.1234)
    #     return x * y * z
    #
    #
    # f = fast(11, 22)
    # s = slow(11, 22, 33)
    # if f != 33:
    #     print('测试失败!')
    # elif s != 7986:
    #     print('测试失败!')

    # 小结
    # 1.请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
    # main()

    # 2.思考一下能否写出一个@log的decorator，使它既支持：
    main()