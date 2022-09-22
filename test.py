#
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Привет! Меня зовут {self.name}!'
#
#     def __repr__(self):
#         return f'Person({repr(self.name)})'
#
#
# p1 = Person('Алексей')
# p2 = exec(repr(p1))
#
#
# # Wife(Person)
# # Husband(Person)
# # Cat
#
# # Controller
# #   make_move(inhabitant)
# # WifeController(Controller)
# #   make_move(wife)
# # HusbandController(Controller)
# #   make_move(husband)
# # CatController(Controller)
# #   make_move(cat)
#
# #
#
# # inhabitants = [Wife(), Husband(), Cat()]
# # for person in inhabitants:
# #     pass
#
# # Basics
# # Functional Programming
# # Object-Oriented Programming
#
# class controller():
#     class wifecontroler():
#
#
# from dataclasses import dataclass
#
#
# @dataclass
# class Smt:
#     name: str
#     age: int
#
#     # self == other
#     def __eq__(self, other):
#         pass
#
#     # hash(self)
#     def __hash__(self):
#         pass


class Person:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height

    def __hash__(self) -> int:
        return hash((self.name, self.age, self.height))


# person1 = Person('viktor', 10, 100)
# person2 = Person('viktor', 10, 100)
# print(hash(person1))
# print(hash(person2))


# def summ(c, d, *, a, b):
#     return a + b
#
# y = [10, 15]
# x = {
#     'a': 5,
#     'b': 10
# }

# print(summ(a=x['a'], b=x['b']))
# print(summ(*y, **x))

# a, *b, c = 10
# print(a, b, c)

#НЕ НУЖНО СТАВИТЬ СКОБКИ ЕСЛИ ничего не наследуюем
#ВСЕ КЛАССЫ С БОЛЬШОЙ БУКВЫ
#СЛЕДИТЬ ЗА НАПИСАНИЕМ КОДА


# selfedu
#
#


class Vehicle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, wheels):
        self.wheels = wheels
        super().__init__(0, 0)

    def move(self) -> None:
        print('Машина едет')

    def a(self):
        pass

# Pascal
# C++
# C
# C#
# JavaScript
# Python
#


class Truck(Car):
    def move(self) -> None:
        super().move()
        print('Но это грузовик')

    def b(self):
        pass


vehicles = [Car(), Truck()]

for vehicle in vehicles:
    vehicle.move()

x = [Car(), Vehicle(), Truck()]

for y in x:
    print(y)


x = 123
b = 321
n = "false"
m = True

a = [x, b, n, m]

for i in a:
    print(i)

print(a)