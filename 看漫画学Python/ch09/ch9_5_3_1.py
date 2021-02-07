# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_5_3_1.py
@time: 2021/1/26 11:19
@desc:
"""
class Dog:
    # 构造方法
    def __init__(self, name, age, sex='雌性'):
        self.name = name # 创建和初始化实例变量name
        self.__age = age # 创建和初始化私有实例变量__age

    # 实例方法
    def run(self):
        print("{0}在跑……".format(self.name))

    # get方法 定义get方法，返回私有实例变量__age
    def get_age(self):
        return self.__age

    # set方法 定义set方法，通过age参数更新私有实例变量__age
    def set_age(self, age):
        self.__age = age

dog = Dog('curry', 2)
print("狗狗的年龄：{}".format(dog.get_age()))
dog.set_age(10)  # 赋值
print("更新年龄后，狗的年龄是:{}".format(dog.get_age()))