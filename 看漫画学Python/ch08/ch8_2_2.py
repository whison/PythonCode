# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_2_2.py
@time: 2020/12/17 14:21
@desc:
"""


def rect_area(width, height):
    area = width * height
    return area


r_area = rect_area(width=320, height=480)
print("{0}*{1}长方形的面积:{2:.2f}".format(320, 480, r_area))

r_area = rect_area(height=480, width=320)
print("{0}*{1}长方形的面积:{2:.2f}".format(320, 480, r_area))
