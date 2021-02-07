# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_7_2.py
@time: 2020/12/18 10:44
@desc:
"""

data = [12, 65, 91, 80, 98, 67]
filtered = filter(lambda x: (x > 50), data)
data1 = list(filtered)
print(data1)
