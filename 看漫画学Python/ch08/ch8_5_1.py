# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_5_1.py
@time: 2020/12/17 15:17
@desc:
"""
x = 20


def print_value():
    global x          #定义一个全局变量
    x = 40
    print("函数中x={0}".format(x))


print_value()
print("全局变量x={0}".format(x))