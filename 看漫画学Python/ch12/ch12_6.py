# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_6.py
@time: 2021/2/2 10:36
@desc:
"""
f_name = '5.jpg'
with open(f_name, 'rb') as f:
    lines = f.readlines()       #  读取所有数据，将数据保存在字节对象lines 中
    copy_f_name = '5_copy.jpg'
    with open(copy_f_name, 'wb') as dest_f_name:    # 以只写模式打开复制后的文件（5_copy.jpg）
        dest_b = dest_f_name.writelines(lines)
        print('复制照片成功！')