# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_6.py
&time: 2020/9/27 9:08
"""


class Banks:
    def __init__(self, username):
        self.name = username
        self.balance = 0
        self.bankname = 'IBC Bank'

    def save_money(self, money):
        self.balance += money
        print("存款：", money, "successful!")

    def withdraw(self, money):
        self.balance -= money
        print("取款：", money, "successful!")

    def get_balance(self):
        print(self.name.title(), "当前余额为:", self.balance)


IbcBank = Banks("whison")
IbcBank.get_balance()
IbcBank.save_money(100000000)
IbcBank.get_balance()
IbcBank.withdraw(50000)
IbcBank.get_balance()
print("当前银行是：", IbcBank.bankname)
IbcBank.balance = 0         #改变私有属性的值
IbcBank.get_balance()
