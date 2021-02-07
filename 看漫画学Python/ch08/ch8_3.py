# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_3.py
@time: 2020/12/17 14:27
@desc:
"""


def make_coffee(name="卡布奇诺"):
    return "制作一杯{0}咖啡。".format(name)


coffce1 = make_coffee("拿铁")
coffce2 = make_coffee()

print(coffce1)
print(coffce2)
