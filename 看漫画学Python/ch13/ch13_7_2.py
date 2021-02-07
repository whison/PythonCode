# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch13_7_2.py
@time: 2021/2/3 9:21
@desc:
"""
import wx  # wx是使用wxPython时要导入的模块


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            None, title="事务处理！", size=(
                300, 180))
        # 创建面板对象，参数parent传递的是self，即设置面板所在父容器为当前窗口对象
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(
            parent=panel,
            label='请单击OK按钮'
        )
        # 创建静态文本（StaticText）对象，将静态文本对象放到panel面板中，所以parent参数传递的是panel,参数label是在静态文本对象上显示的文字
        b = wx.Button(parent=panel, label='OK')
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

        # 创建垂直方向的盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到vbox布局管理器
        vbox.Add(self.statictext,proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
        # 添加按钮b到vbox布局管理器
        vbox.Add(b,proportion=1, flag=wx.EXPAND|wx.BOTTOM,border=10)
        # 设置面板（panel）采用vbox布局管理器
        panel.SetSizer(vbox)        # 两个控件都被放到面板中，所以需要设置面板布局为盒子布局

    def on_click(self, event):
        self.statictext.SetLabelText('mohuisheng')


# 创建应用程序对象
app = wx.App()
# 创建窗口对象
frm = MyFrame()
# 显示窗口
frm.Show()  # 窗口默认隐藏，需要调用Show()方法才能显示
# 进入主事件循环
app.MainLoop()  # 让应用进入主事件循环中