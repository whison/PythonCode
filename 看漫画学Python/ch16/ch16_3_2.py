# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch16_3_2.py
@time: 2021/2/7 10:10
@desc:
"""
import threading
import time

class SmallThread(threading.Thread):    # 自定义线程类，继承Thread类
    def __init__(self, name=None):   #定义线程类的构造方法，name参数是线程名
        super().__init__(name=name)
    #线程体函数
    def run(self):  # 重写父类Thread的run()方法
    # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第{0}次执行线程{1}'.format(n, t.name))
            # 线程休眠
            time.sleep(2)    # 在多线程编程时，要注意给每个子线程执行的机会，主要是通过让子线程休眠来让当前线程暂停执行，其他线程才有机会执行。如果子线程没有休眠，则基本上在第1个子线程执行完毕后，再执行第2个子线程。
        print('线程{0}执行完成！'.format(t.name))

# 主线程
# 创建线程对象t1
t1 = SmallThread()    # 通过自定义线程类，创建线程对象
# 创建线程对象t2
t2 = SmallThread(name='MyThread')  # 设置线程名
# 启动线程t1
t1.start()
# 启动线程t2
t2.start()