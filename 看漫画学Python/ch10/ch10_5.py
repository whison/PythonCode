# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch10_5.py
@time: 2021/1/26 15:36
@desc:
"""
class YZ_Exception(Exception):
    def __init__(self, message):    # 构造方法，其中的参数message是异常描述信息
        super().__init__(message)   # 调用父类构造方法，并把参数message付给父类构造方法

i = input('请输入数字：')
n = 888
try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n, i, result))
except ZeroDivisionError as e:
    # print("不能除以0，异常：{}".format(e))
    raise YZ_Exception('除数为0了，请检查！')
except ValueError as e:
    # print("输入的是无效数字，异常：{}".format(e))
    raise YZ_Exception('输入无效数字！')