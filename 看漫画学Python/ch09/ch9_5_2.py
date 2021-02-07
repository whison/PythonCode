# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_5_2.py
@time: 2021/1/25 17:19
@desc:
"""
class Account:
    __interest_rate = 0.0568  # 私有类变量利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner  # 创建并初始化实例变量owner
        self.__amount = amount    # 创建并初始化私有实例变量__amount

    def __get_info(self):   # 定义私有方法
        print("{0}金额：{1}；利率：{2}！".format(self.owner, self.__amount, self.__interest_rate))

    def desc(self):         # 在类内部可以调用私有方法
        print(self.__get_info())

account = Account('curry', 50000000)
account.desc()

account.__get_info()        # 在类外部调用私有方法，则发生错误
