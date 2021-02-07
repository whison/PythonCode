# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_4_3.py
@time: 2021/1/25 14:21
@desc:
"""


class Dog:
    def __init__(self, name, age, sex='雌性'):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age
        self.sex = sex  # 创建和初始化实例变量sex

    def run(self):
        print("{}在跑……".format(self.name))

    def speak(self, sound):
        print('{}在叫，"{}"!'.format(self.name, sound))


dog = Dog('curry', 2)
dog.run()
dog.speak('Wang Wang Wang')
