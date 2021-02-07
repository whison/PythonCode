# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch10_4.py
@time: 2021/1/26 15:31
@desc:自定义异常类
"""
class YZ_Exception(Exception):
    def __init__(self, message):    # 构造方法，其中的参数message是异常描述信息
        super().__init__(message)   # 调用父类构造方法，并把参数message付给父类构造方法