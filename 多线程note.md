# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf、
# 多线程 vs 多进程
- 程序：一堆代码以文本形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据线等
    - 每个进程有自己独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释锁（GIL）
    - python代码执行时由python虚拟机进行控制
    - 在主循环中之内更有一个控制线程在执行
    
- python的包
    - threading 通行的包
    - 案例01顺序执行，耗时比较长
    - 案例02，改用多线程，缩短总时间，用_thread
    