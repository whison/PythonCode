# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_4_1.py
@time: 2021/1/25 12:00
@desc:
"""


class Dog:
    def __init__(self, name, age, sex='雌性'):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age
        self.sex = sex # 创建和初始化实例变量sex

d1 = Dog('旺旺', 2)
d2 = Dog('哈哈', 1, '阴阳')
d3 = Dog(name='curry', sex='杂种', age=4)
print('{0}：{1}岁{2}！'.format(d1.name, d1.age, d1.sex))
print('{0}：{1}岁{2}！'.format(d2.name, d2.age, d2.sex))
print('{0}：{1}岁{2}！'.format(d3.name, d3.age, d3.sex))
