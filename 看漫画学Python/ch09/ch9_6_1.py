# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_6_1.py
@time: 2021/1/26 11:59
@desc:继承
"""


class Animal:
    def __init__(self, name):
        self.name = name        # 初始化父类的实例成员变量

    def show_info(self):
        return "动物的名字：{}".format(self.name)

    def move(self):
        print("动一动......")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类构造方法，初始化父类成员变量
        self.age = age      # 初始化子类的实例成员变量


cat = Cat('Tom', 2)
cat.move()
print(cat.show_info())
