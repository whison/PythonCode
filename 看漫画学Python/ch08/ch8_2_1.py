# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_2_1.py
@time: 2020/12/17 14:14
@desc:
"""

def rect_area(width, height):
    area = width * height
    return area

r_area = rect_area(32.6, 48.70)
print("{0} * {1}长方形的面积:{2:.2f}".format(32.6, 48.70,r_area))