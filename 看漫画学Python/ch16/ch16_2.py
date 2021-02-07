# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch16_2.py
@time: 2021/2/7 10:22
@desc:
"""
import threading
# 当前线程对象
t = threading.current_thread()  # 在运行过程中只有一个线程，就是主线程，因此当前线程是主线程
# 当前线程名
print(t.name)

# 返回当前处于活动状态的线程个数
print(threading.active_count())  # 在运行过程中只有一个线程，活动状态的线程只有一个

# 当主线程对象
t = threading.main_thread()     # 主线程和当前线程是同一个
# 主线程名
print(t.name)
