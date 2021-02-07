# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch10_1.py
@time: 2021/1/26 13:55
@desc: 在python中，异常类命名的主要后缀有Exception、Error和Warning
"""

i = input('请输入数字：')
n = 888
result = n / int(i)
print(result)
print('{0}除以{1}等于{2}'.format(n, i, result))