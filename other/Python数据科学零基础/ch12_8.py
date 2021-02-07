# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_8.py
@time: 2020/9/27 14:42
@desc:私有属性
"""


class Banks:
    def __init__(self, username):
        self.__name = username
        self.__balance = 0
        self.__bankname = 'IBC Bank'

    def save_money(self, money):
        self.__balance += money
        print("存款：", money, "successful!")

    def withdraw(self, money):
        self.__balance -= money
        print("取款：", money, "successful!")

    def get_balance(self):
        print(self.__name.title(), "当前余额为:", self.__balance)


IbcBank = Banks("whison")
IbcBank.get_balance()
IbcBank.save_money(100000000)
IbcBank.get_balance()
IbcBank.withdraw(50000)
IbcBank.get_balance()
IbcBank.__balance = 0     #不能改变私有属性的值
IbcBank.get_balance()
IbcBank.__Banks
