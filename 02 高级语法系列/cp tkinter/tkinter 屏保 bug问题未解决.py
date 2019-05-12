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
import random
import tkinter as tk
class Ball():

    def __init__(self,canvas,screenwidth,screenheight):
        self.canvas=canvas
        # 球的出生位置
        self.xpos = random.randint(10,int(screenwidth)-20)
        self.ypos = random.randint(10,int(screenheight)-20)
        # 球的运动速度
        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)
        # 球的大小
        # 设定球的半径
        self.radius = random.randint(20,70)
        # 初始化长和宽
        self.screenwidth = screenheight
        self.screenheight = screenheight
        # 球的颜色
        c = lambda :random.randint(0,255)
        self.color = "#%02x%02x%02x"%(c(),c(),c())
    def creat_ball(self):

        x1 = self.xpos-self.radius
        x2 = self.xpos+self.radius
        y1 = self.ypos-self.radius
        y2 = self.ypos+self.radius

        self.item = self.canvas.create_oval(x1,y1,x2,y2,fill = self.color,
                                            outline =self.color )
    def move_ball(self):

        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都有一个新的坐标
        # 球的新位置等于原来的位置加上球的移动速递
        self.xpos = self.xpos+self.xvelocity
        self.ypos = self.ypos+self.yvelocity
        # 普安段球是否撞墙
        if  self.xpos+self.radius >= self.screenwidth:
            self.xvelocity = -self.xvelocity
        if self.xpos-self.radius <= self.screenwidth:
            self.xvelocity = self.xvelocity
        if self.ypos-self.radius<=self.screenheight:
            self.yvelocity = -self.yvelocity
        if self.ypos+self.radius >= self.screenheight:
            self.yvelocity = self.yvelocity

        self.canvas.move(self.item,self.xvelocity,self.yvelocity)

class ScreenSaver():
    balls = list()
    def __init__(self):

        # 每次启动球的数量随机
        self.num_balls = random.randint(6,20)
        # 设定屏保窗口大小

        self.root = tk.Tk()
        # 取消边框
        self.root.overrideredirect(1)
        # 任何鼠标移动都可以取消
        self.root.bind("<Motion>",self.myquit)
        self.root.bind("<Key>",self.myquit)

        # 得到屏幕大小规格
        self.w = self.root.winfo_width()
        self.h = self.root.winfo_height()
        #创建画布,包括画布的归属规格
        self.canvas = tk.Canvas(self.root,width=self.w,height=self.h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(0,self.num_balls):
            ball = Ball(self.canvas,screenwidth=self.w,screenheight=self.h)
            ball.creat_ball()
            self.balls.append(ball)
        self.Run_Sreen_Saver()
        self.root.mainloop()

    # 让屏保动起来

    def Run_Sreen_Saver(self):
        for ba1l in self.balls:
            ba1l.move_ball()
        # after是200毫秒后启动一个函数，需要启动的函数是第二个参数
        self.canvas.after(200,self.Run_Sreen_Saver)

    def myquit(self):
        # 销毁退出
        self.root.destroy()

if __name__ == '__main__':
    ScreenSaver()
