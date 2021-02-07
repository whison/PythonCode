# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch9_7.py
@time: 2021/1/26 13:48
@desc:多态性
"""


def start(obj):
    obj.speak()


class Animal:
    def speak(self):
        print('动物叫，但不知道是哪种动物叫！')


class Dog(Animal):
    def speak(self):
        print('小狗：旺旺叫......')


class Cat(Animal):
    def speak(self):
        print('小猫：喵喵叫......')


class Car:
    def speak(self):
        print('小汽车：嘀嘀叫......')


start(Dog())
start(Cat())
start(Car())