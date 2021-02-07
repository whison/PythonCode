# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch16_3_1.py
@time: 2021/2/7 9:43
@desc:
"""
import threading
import time

#线程体函数
def thread_body():
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
t1 = threading.Thread(target=thread_body)    # 指定线程体的函数名，注意在函数名后面不要跟小括号
# 创建线程对象t2
t2 = threading.Thread(target=thread_body, name='MyThread')  # 设置线程名
# 启动线程t1
t1.start()
# 启动线程t2
t2.start()