# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_4_5.py
@time: 2021/1/25 14:52
@desc:
"""
class Account:
    interest_rate = 0.0668  # 类变量利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner  # 创建并初始化实例变量owner
        self.amount = amount    # 创建并初始化实例变量amount


    # 类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

interest = Account.interest_by(120000)
print('计算利息：{0:.3f}'.format(interest))



account = Account('curry', 50000000)

print('帐户名：{0}'.format(account.owner))
print('帐户金额:{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))