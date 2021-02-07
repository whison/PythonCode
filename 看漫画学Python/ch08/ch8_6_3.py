# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_6_3.py
@time: 2020/12/17 16:14
@desc:
"""


def f1(x):
    return x * 2  # 变换规则乘以2


data = [2, 5, 6, 7, 4, 9, 25]
mapped = map(f1, data)
data1 = list(mapped)  # 转换为列表
print(data1)
