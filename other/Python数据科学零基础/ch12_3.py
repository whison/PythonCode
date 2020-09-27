# _*_ coding utf-8 _*_
'''
@author: mohui
@software: PyCharm
@file: ch12_3.py
&time: 2020/9/26 17:22
'''


class Banks:
    BankName = 'ABC Bank'

    def __init__(self, username, money):
        self.name = username
        self.balance = money

    def get_balance(self):
        return self.balance


AbcBank = Banks('whison', 10000000)
print(AbcBank.name.title(), "存款余额是", AbcBank.get_balance())
