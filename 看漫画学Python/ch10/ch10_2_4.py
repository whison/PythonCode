# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch10_2_4.py
@time: 2021/1/26 15:14
@desc:try-except嵌套，尽量不要用！
"""
i = input('请输入数字：')
n = 888

try:
    i2 = int(i)
    try:
        result = n / int(i)
        print(result)
        print('{0}除以{1}等于{2}'.format(n, i, result))
    except ZeroDivisionError as e:
        print("不能除以0，异常：{}".format(e))
except ValueError as e:
    print("输入的是无效数字，异常：{}".format(e))