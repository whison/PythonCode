# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_6_3.py
@time: 2021/1/26 12:51
@desc: 方法重写
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

    # 重写父类方法show_info()
    def show_info(self):
        return "骡：{0}，{1}岁。".format(self.name, self.age)


le = Mule('骡宝莉', 10)
le.run()    # 继承父类Horse方法
le.roll()   # 继承父类Donkey方法
print(le.show_info())   # 子类Mule自己的方法
