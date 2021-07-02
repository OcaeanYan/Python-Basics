# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        # self.__name = name  # 要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
        # self.__score = score  # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
        self.__name = name
        self.__gender = gender

    # def print_score(self):
    #     print('%s: %s' % (self.__name, self.__score))
    #
    # def get_name(self):
    #     return self.__name
    #
    # def get_score(self):
    #     return self.__score
    #
    # def set_score(self, score):
    #     if 0 <= score <= 100:
    #         self.__score = score
    #     else:
    #         raise ValueError('bad score')

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


if __name__ == '__main__':
    james = Student('Lakes', 23)

    # 测试:
    bart = Student('Bart', 'male')
    print(bart.get_gender())
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')
