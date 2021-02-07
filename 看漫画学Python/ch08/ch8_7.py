# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_7.py
@time: 2020/12/18 10:36
@desc:
"""


def calc(opr):
    if opr == '+':
        return lambda a, b: (a + b)    # 替代add()函数
    else:
        return lambda a, b: (a - b)    # 替代sub()函数


f1 = calc('+')
f2 = calc('-')
print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
