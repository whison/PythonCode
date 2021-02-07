# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_6_1.py
@time: 2020/12/17 15:27
@desc:
"""

# 定义加法函数


def add(a, b):
    return a + b

# 定义减法函数


def sub(a, b):
    return a - b
# 定义平方函数


def square(a):
    return a * a

# 定义计算函数


def calc(opr):
    if opr == '+':
        return add
    elif opr == '-':
        return sub
    else:
        return square


f1 = calc('+')
f2 = calc('-')
f3 = calc('*')

print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
print("10 * 10 = {0}".format(f3(10)))
