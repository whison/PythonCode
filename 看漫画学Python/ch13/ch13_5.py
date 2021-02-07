# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch13_5.py
@time: 2021/2/2 14:47
@desc:
"""
import wx  # wx是使用wxPython时要导入的模块


# 自定义窗口类MyFrame


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            None, title="第一个wxPython程序！", size=(
                400, 300), pos=(
                100, 100))
        panel = wx.Panel(parent=self) # 创建面板对象，参数parent传递的是self，即设置面板所在父容器为当前窗口对象
        self.statictext = wx.StaticText(
            parent=panel,
            label='Hello World',
            pos=(
                30,
                40))        # 创建静态文本（Static Text）对象，将静态文本对象放到panel面板中，所以parent参数传递的是panel,参数label是在静态文本对象上显示的文字，参数pos用于设置静态文本对象的位置
        # 你的代码


# 创建应用程序对象
app = wx.App()
# 创建窗口对象
frm = MyFrame()
# 显示窗口
frm.Show()  # 窗口默认隐藏，需要调用Show()方法才能显示
# 进入主事件循环
app.MainLoop()  # 让应用进入主事件循环中
