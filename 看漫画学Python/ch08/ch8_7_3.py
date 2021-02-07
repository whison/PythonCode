# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_7_3.py
@time: 2020/12/18 10:45
@desc:
"""
data = [2, 5, 6, 7, 4, 9, 25]
mapped = map(lambda x: (x * 2), data)
data1 = list(mapped)  # 转换为列表
print(data1)
