"""
Kinter项目实战-屏保
项目分析
- 屏保可以自己启动，也可以手动启动
- 一旦敲击键盘或者移动鼠标后，或者其他的引发时间，则停止
- 如果屏保是一幅画的话，则没有画框
- 图像的动作是随机的，具有随机性，可能包括颜色，大小，多少， 运动方向，变形等
- 整个世界的构成是：
    - ScreenSaver:
        - 需要一个canvas， 大小与屏幕一致，没有边框

    - Ball
        - 颜色，大小，多少， 运动方向，变形等随机
        - 球能动，可以被调用
"""
import random,tkinter
class Ball():
    def __init__(self,canvas,screenwidth,screenheight):
        # 初始化屏幕的大小
        self.screenwidth=screenwidth
        self.screenheight=screenheight

        # 且出现的初始位置的坐标
        self.xpos = random.randint(10,int(screenwidth)-20)
        self.ypos = random.randint(10,int(screenheight)-20)

        # 定义球的运动速度
        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)

        # 定义球的大小
        # 球的大小由圆心减去半径
        self.radius = random.randint(30,120)

        # 定义颜色
        # 颜色由rgb表示
        c = lambda: random.randint(0,255)
        self.color = '#%02x%02x%02x'%(c(), c(), c())
