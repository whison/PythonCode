# _*_ coding utf-8 _*_
'''
@author: mohui
@software: PyCharm
@file: ch12_3.py
&time: 2020/9/26 17:22
'''
class Banks():
    bankname = 'ABC Bank'
    def __init__(self, username, money):
        self.name = username
        self.balance = money

    def get_balance(self):
        return self.balance
whison_bank = Banks('whison', 10000000)
print(whison_bank.name.title(), "存款余额是", whison_bank.get_balance())