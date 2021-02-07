# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch8_4_2.py
@time: 2020/12/17 14:32
@desc:
"""


def show_info(**info):
    print('------show_information--------')
    for key, value in info.items():
        print('{0}-{1}'.format(key, value))


show_info(name='whison', age=33, sex=True)
show_info(student_name='mohuisheng', student_no='10086')
