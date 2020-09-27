# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_4.py
&time: 2020/9/27 8:48
"""


class Banks:
    """
    定义银行
    """
    BankName = 'ABC Bank'   # 定义属性

    def __init__(self, username, money):    # 初始化方法
        self.name = username    # 设置存款都的名字
        self.balance = money    # 设置所存的钱

    def save_money(self, money):
        self.balance += money
        print("存款", money, "完成")

    def withdraw_money(self, money):
        self.balance -= money
        print("取款", money, "完成")

    def get_balance(self):
        print(self.name.title(), "目前余额：", self.balance)


AbcBank = Banks("whison", 100000000000000)
AbcBank.get_balance()
AbcBank.save_money(5000000)
AbcBank.get_balance()
AbcBank.withdraw_money(10000)
AbcBank.get_balance()
