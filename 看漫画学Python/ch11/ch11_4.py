# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch11_4.py
@time: 2021/1/30 11:50
@desc:
"""
import re

p = r'\d+'
text = "AB12CD34EF"
repace_text = re.sub(p, ' ', text)  # sub函数省略参数count时，表示不限制替换数量
print(repace_text)

p = r'\d+'
text = "AB12CD34EF"
repace_text = re.sub(p, ' ', text, count=1)  # sub函数指定参数count=1时，表示替换1次
print(repace_text)

p = r'\d+'
text = "AB12CD34EF"
repace_text = re.sub(p, ' ', text, count=2)  # sub函数指定参数count=1时，表示替换2次
print(repace_text)