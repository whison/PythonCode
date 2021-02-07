# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_5_1.py
@time: 2021/1/25 16:56
@desc:
"""
class Account:
    __interest_rate = 0.0568  # 私有类变量利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner  # 创建并初始化实例变量owner
        self.__amount = amount    # 创建并初始化私有实例变量__amount

    def desc(self): # 在类的内部可以访问私有变量
        print("{0}金额：{1}；利率：{2}！".format(self.owner, self.__amount, self.__interest_rate))
account = Account('curry', 50000000)
account.desc()

print('帐户名：{0}'.format(account.owner))
print('帐户金额:{0}'.format(account.__amount))         # 在类外部不可以访问私有变量
print('利率：{0}'.format(Account.__interest_rate))    # 在类外部不可以访问私有变量