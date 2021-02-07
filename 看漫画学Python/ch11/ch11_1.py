# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch11_1.py
@time: 2021/1/26 17:05
@desc:
"""
import datetime
d = datetime.datetime.today()
c = d.strftime('%Y-%m-%d %H:%M:%S')
a = d.strftime('%Y-%m-%d')
print(c)
print(a)

str_date = '2020-10-01 11:11:11'
b = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print(b)