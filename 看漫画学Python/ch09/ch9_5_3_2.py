# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_5_3_2.py
@time: 2021/1/26 11:31
@desc:
"""


class Dog:
    # 构造方法
    def __init__(self, name, age, sex='雌性'):
        self.name = name  # 创建和初始化实例变量name
        self.__age = age  # 创建和初始化私有实例变量__age

    # 实例方法
    def run(self):
        print("{0}在跑……".format(self.name))

    # 定义age属性的get()方法，使用@property装饰器进行修饰，方法名就是属性名，即age
    @property
    def age(self):
        return self.__age

    # 定义age属性的set()方法，使用@age.setter装饰器进行修饰，age是属性名
    @age.setter
    def age(self, age):
        self.__age = age


dog = Dog('curry', 2)
print("狗狗的年龄：{}".format(dog.age))   # 可以通过属性取值，访问形式为”实例.属性“
dog.age = 20 # 可以通过属性赋值，访问形式为”实例.属性“
print("更新年龄后，狗的年龄是:{}".format(dog.age))