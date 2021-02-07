# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch13_3.py
@time: 2021/2/2 14:32
@desc:
"""
import wx       # wx是使用wxPython时要导入的模块
# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = wx.Frame(None, title='第一个wxPython程序', size=(400, 300), pos=(100, 100))    # None 位置为所在窗口，None表示没有父窗口，size表示窗口的大小，pos表示窗口的位置
# 显示窗口
frm.Show()      # 窗口默认隐藏，需要调用Show()方法才能显示
# 进入主事件循环
app.MainLoop()   # 让应用进入主事件循环中
