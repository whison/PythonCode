# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch11_5.py
@time: 2021/1/30 11:58
@desc:
"""
import re

p = r'\d+'
text = "AB12CD34EF"
repace_text = re.split(p, text)  # split函数省略参数maxsplit时，表示分割的次数没有限制
print(repace_text)

p = r'\d+'
text = "AB12CD34EF"
repace_text = re.split(p, text, maxsplit=1)  # split函数省略参数maxsplit时，表示分割1次
print(repace_text)

p = r'\d+'
text = "AB12CD34EF"
repace_text = re.split(p, text, maxsplit=2)  # split函数省略参数maxsplit时，表示分割2次
print(repace_text)
