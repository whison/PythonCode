# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch11-3.py
@time: 2021/1/28 16:53
@desc:
"""
import re

p = r'\w+@zhijieketang\.com'
text = "Tony's email is tony_guan588@zhijieketang.com"
m = re.search(p, text)
print(m)  # <re.Match object; span=(16, 45), match='tony_guan588@zhijieketang.com'>  输出match对象，找到子字符串，开始位置索引是16，结束位置索引是45
text = "Tony's email is tony_guan588@163.com"
m = re.search(p,text)
print(m)

p = r'Python|python|PYTHON'    # 验证Java单词的正则表达式，正则表达式中的竖线（|）字符表示”或“关系
text = 'I like Python and python and PYTHON.'
match_list = re.findall(p, text) # 返回匹配的字符串列表
print(match_list)