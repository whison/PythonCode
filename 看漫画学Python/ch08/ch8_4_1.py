# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_4_1.py
@time: 2020/12/17 14:37
@desc:
"""


def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total


print(sum(100.0, 22.4, 45.3))
print(sum(12345.43, 8766.43))
