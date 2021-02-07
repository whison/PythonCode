# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_2.py
@time: 2021/2/1 17:18
@desc:对文件的操作往往会抛出异常，为了保证对文件的操作无论是正常结束还异常结束，都能够关闭文件，我们应该将对close（ ）方法的调用放在异常处理的finally代码块中。
"""

f_name = 'test.txt'
f = None
try:
    f = open(f_name)
    print("打开文件成功")
    contect = f.read()
    print(contect)
except FileNotFoundError as e:
    print("文件不存在，请先使用ch12_1.py程序创建文件")
except OSError as e:
    print('处理OSError异常')
finally:
    if f is not None:
        f.close()
        print("关闭文件成功！")