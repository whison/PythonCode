# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch10_2_3.py
@time: 2021/1/26 15:11
@desc:
"""
i = input('请输入数字：')
n = 888
try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n, i, result))
except (ZeroDivisionError, ValueError) as e:
    print("异常发生了：{}！".format(e))
