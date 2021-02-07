# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_2_2.py
@time: 2021/2/1 17:24
@desc: with as 代码块，可帮助我们自动释放资源（包括关闭文件的操作），它可以替代finally代码块，优化代码结构，提高可读性
"""

f_name = 'test.txt'
with open(f_name) as f:
    contect = f.read()
    print(contect)