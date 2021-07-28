
# __len__()方法我们也知道是为了能让class作用于len()函数。
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#     __repr__ = __str__


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __ne

if __name__ == '__main__':

# __len__()方法我们也知道是为了能让class作用于len()函数。
#     print(Student('Michael'))
#     s = Student('Kobe')