# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch11_2.py
@time: 2021/1/27 14:44
@desc:
"""
import re
p = r'\w+@163\.com'
email = 'tony_guan123@163.com'
m = re.match(p, email)
print(type(m))  # 返回非空的Match对象，说明匹配成功
print(m)

email2 = 'mohuisheng@126.com'
m1 = re.match(p, email2)
print(m1)