# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_1.py
@time: 2021/2/1 8:56
@desc: a 只能追加写入文件，不可读文件；而a+既可以追加写入文件，也可以读文件
"""

f = open('test.txt', 'w+')      # 以W+模式打开文件，如果不存在，则创建该文件
f.write('现在以写模式打开文件，如果不存在，就创建该文件')
print('1、创建test.txt文件，word写入文件')

f = open('test.txt', 'r+')
f.write('现在以读模式打开文件，由于第10行已经创建了该文件，所以会覆盖文件的内容')
print('2、打开test.txt文件，原内容被覆盖掉！')

f = open('test.txt', 'a')
f.write('现在以追加模式打开文件，会在文件末尾追加内容')
print('3、打开test.txt文件，会在文件末尾追加内容！')

fname = './test.txt'
f = open(fname, 'a+')
f.write('mohuisheng')
print('4、打开test.txt文件，会在文件末尾追加内容mohuisheng！')