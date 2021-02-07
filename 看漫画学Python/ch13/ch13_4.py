# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch13_4.py
@time: 2021/2/2 14:41
@desc:
"""
import wx       # wx是使用wxPython时要导入的模块

# 自定义窗口类MyFrame


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            None, title="第一个wxPython程序！", size=(
                400, 300), pos=(
                100, 100))
        # 你的代码


# 创建应用程序对象
app = wx.App()
# 创建窗口对象
frm = MyFrame()
# 显示窗口
frm.Show()      # 窗口默认隐藏，需要调用Show()方法才能显示
# 进入主事件循环
app.MainLoop()   # 让应用进入主事件循环中
