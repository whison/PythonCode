# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_6_2.py
@time: 2021/1/26 12:07
@desc: 多继承
"""


class Horse:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "马的名字：{}".format(self.name)

    def run(self):
        print("马在跑......")


class Donkey:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("驴的名字：{}".format(self.name))

    def run(self):
        print("驴在跑......")

    def roll(self):
        print("驴打滚......")


class Mule(Horse, Donkey):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


le = Mule('骡宝莉', 10)
le.run()    # 继承父类Horse方法
le.roll()   # 继承父类Donkey方法
print(le.show_info())   # 继承父类Horse方法
