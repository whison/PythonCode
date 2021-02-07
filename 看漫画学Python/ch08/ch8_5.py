# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_5.py
@time: 2020/12/17 15:14
@desc:
"""


x = 20


def print_value():
    x = 10
    print("函数中x={0}".format(x))


print_value()
print("全局变量x={0}".format(x))
