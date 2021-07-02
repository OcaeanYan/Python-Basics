# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name , score):
        self.name = name
        self.score = score

# 数据封装
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    james = Student('Lakes', 23)
    james.print_score()
    print(james.get_grade())

    # 练习题: 同样的，get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节
    lisa = Student('Lisa', 99)
    bart = Student('Bart', 59)
    print(lisa.name, lisa.get_grade())
    print(bart.name, bart.get_grade())