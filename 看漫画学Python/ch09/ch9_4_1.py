# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_4_1.py
@time: 2021/1/25 12:00
@desc:
"""


class Dog:
    def __init__(self, name, age):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age


d = Dog('旺旺', 2)
print('我们家狗狗名叫{0},{1}岁了！'.format(d.name, d.age))
