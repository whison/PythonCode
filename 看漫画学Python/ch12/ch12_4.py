# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch12_4.py
@time: 2021/2/2 10:22
@desc:文本文件复制
"""
f_name = './test.txt'
with open(f_name,'r', encoding='GBK') as f:     #  以只读模式打开文本文件，注意文件编码形式是GBK,与字符集的大小写没关系
    lines = f.readlines()   # 读取所有数据到一个列表中
    copy_f_name = 'dest_test.txt'
    with open(copy_f_name, 'w', encoding='utf-8') as dest_f:        #  以只写模式打开文本文件，注意文件编码形式是UTF-G
        dest_f.writelines(lines)    # 把列表数据Lines 写入文件中
        print('文件复制成功！')