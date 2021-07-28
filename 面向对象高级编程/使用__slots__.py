from types import MethodType


# class Student(object):
#     pass
#
# def set_age(self, age):  # 定义一个函数作为实例方法
#     self.age = age
#
# def set_score(self, score):
#     self.score = score
#

class Student(object):
    __slots__ = ('name', 'age', 'score') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

if __name__ == '__main__':
    # 可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
    # s = Student()
    # s.name = 'Kobe'  # 动态给实例绑定一个属性
    # print(s.name)
    #
    # s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
    # s.set_age(25)   # 调用实例方法
    # print(s.age)    # 测试结果

    # s2 = Student() # 创建新的实例
    # s2.set_age(25) # 尝试调用方法

    s = Student()
    s.name = 'Kobe'
    s.age = 24
    s.score = 81
    print(s.name, s.score, s.age)

    g = GraduateStudent()
    g.score = 9999
    print(g.score)