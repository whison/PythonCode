# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch13_8_1.py
@time: 2021/2/3 10:20
@desc:文本输入控件（wx.TextCtrl）是可以输入文本的控件！实现三个文本输入控件和三个静态文本！
"""
import wx

# 自定义窗口类MyFrame


class MyFrame(wx.Frame):
    def __init__(self):
        super(MyFrame, self).__init__(None, title="文本输入控件", size=(300, 460))
        panel = wx.Panel(parent=self)
        tc1 = wx.TextCtrl(panel)    # 创建变通文本输入控件
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)   # 创建密码输入控件
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)  # 创建多行文本输入控件

        userid = wx.StaticText(panel, label="用户ID")
        pwd = wx.StaticText(panel, label="密码")
        content = wx.StaticText(panel, label="多行文本：")

        # 创建垂直方向的盒子布局管理器vbox对象
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加userid到vbox布局管理器
        vbox.Add(userid,  flag=wx.EXPAND | wx.LEFT, border=10)
        # 添加tc1到vbox布局管理器
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        # 添加pwd到vbox布局管理器
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        # 添加tc2到vbox布局管理器
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        # 添加content到vbox布局管理器
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        # 添加tc3到vbox布局管理器
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)

        # 设置面板（panel）采用vbox布局管理器
        panel.SetSizer(vbox)

        # 设置tc1初始值
        tc1.SetValue('mohuisheng')      # 设置文本输入控件的内容
        # 获取tc1值
        print('读取用户ID:{}'.format(tc1.GetValue()))        # 获取文本输入控件的内容


# 创建应用程序对象
app = wx.App()
# 创建窗口对象
fram = MyFrame()
# 显示窗口
fram.Show()
# 进入主事件循环
app.MainLoop()