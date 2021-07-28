# class Animal(object):
#     pass
#
# # 大类:
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# # 各种动物:
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Running...')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
#
# class Dog(Mammal, Runnable):
#     pass
#
# class Bat(Mammal, Flyable):
#     pass
#
# # 编写一个多进程模式的TCP服务，定义如下：
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
#
# # 编写一个多线程模式的UDP服务，定义如下：
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
#
# # 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass
