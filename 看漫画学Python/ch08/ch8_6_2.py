# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_6_2.py
@time: 2020/12/17 15:56
@desc:
"""

def f1(x):
    return x > 50  # 找出大于50的元素

data = [12, 65, 91, 80, 98, 67]
filtered = filter(f1, data)
data1 = list(filtered)
print(data1)