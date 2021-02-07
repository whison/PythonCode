# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch16_4_2.py
@time: 2021/2/7 11:05
@desc:
"""
import threading
import time

# 线程停止变量
isrunning = True        # 创建一个线程停止变量isrunning, 控制线程结束
# 工作线程体函数


def workthread_body():  # 工作线程体执行一些任务
    while isrunning:    # 工作线程体“死循环”
        # 线程开始工作
        print('工作线程执行中……')
        # 线程休眠
        time.sleep(5)
    print('工作线程结束。')

# 控制线程体函数


def controlthread_body():       # 控制线程体从控制台读取指令，根据指令修改线程停止变量
    global isrunning        # 由于需要在线程体中修改变量isrunning，因此需要将isrunning变量声明为global
    while isrunning:        # 控制线程体“死循环”
        #   从键盘输入停止指令exit
        command = input('请输入停止指令：')
        if command == 'exit':
            isrunning = False
            print('控制线程结束。')


# 主线程
# 创建工作线程对象workthread
workthread = threading.Thread(target=workthread_body)       # 工作线程用来执行一些任务
# 启动线程workthread
workthread.start()
# 创建控制线程对象controlthread
controlthread = threading.Thread(
    target=controlthread_body)     # 控制线程控制修改线程停止变量
# 启动线程controlthread
controlthread.start()
