# _*_ coding utf-8 _*_
"""
@author: mohuisheng
@software: PyCharm
@file: ch16_4_1.py
@time: 2021/2/7 10:53
@desc:
"""
import threading
import time

# 共享变量
value = []      # 定义一个共享变量value，该变量是多个线程都可以访问的变量
# 线程体函数
def thread_body():
    # 当前线程对象
    print('t1子线程开始……')
    for n in range(2):
        print('t1子线程执行……')
        value.append(n)     # 在子线程体中修改变量value的内容
        time.sleep(2)
    print('t1子线程结束。')

# 主线程
print('主线程开始执行……')
# 创建线程对象t1
t1 = threading.Thread(target=thread_body)
# 启动线程t1
t1.start()
# 主线程补阻塞，等待t1线程结束
t1.join()       # 在当前线程（主线程）中调用t1的join()方法，因此会导致当前线程阻塞，等待t1线程结束
print('vaule={0}'.format(value))  # t1 线程结束，继续执行，访问并输出变量value
print('主线程继续执行……')