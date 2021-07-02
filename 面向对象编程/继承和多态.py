class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog is Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    def run(self):
        print('Start...')


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    dog.eat()

    cat = Cat()
    cat.run()

    run_twice(Tortoise())

    test = Timer()
    test.run()
