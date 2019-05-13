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
from random import randint
from tkinter import *
class Ball():

    def __init__(self,canvas,scrnwidth,scrnheight):
        self.canvas = canvas
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        # 球的坐标
        self.xpos = randint(10,int(scrnwidth))
        self.ypos = randint(10,int(scrnheight))

        # 球的速度
        self.x_move = randint(10,20)
        self.y_move = randint(15,25)

        # 球的颜色
        c = lambda :randint(0,255)
        self.color = "#%02x%02x%02x"%(c(),c(),c())
        # 球的半径
        self.radius = randint(20,70)
    def creat_canvas(self):
        # 球的坐标
        x1 = self.radius+self.xpos
        x2 = self.radius-self.xpos
        y1 = self.radius-self.ypos
        y2 = self.radius+self.ypos
        self.ovel = self.canvas.creat_oval(x1,y1,x2,y2,fill=self.color,
                                           outline=self.color)
        # 球的移动
    def move_ball(self):

        self.xpos +=self.x_move
        self.ypos +=self.y_move

        if self.xpos >= self.scrnwidth - self.radius:
            self.x_move = -self.x_move
        if self.ypos >= self.scrnheight - self.radius:
            self.y_move = -self.y_move
        if self.xpos < self.radius:
            self.x_move = abs(self.x_move)
        if self.ypos < self.radius:
            self.y_move = abs(self.y_move)
        self.canvas.move(self.ovel,self.x_move,self.y_move)

class ScreenSaver():
    balls = []
    def __init__(self):

        self.ball_nums = randint(20,40)
        self.window = Tk()
        self.window.overrideredirect(True)
        self.winth = self.window.winfo_width()
        self.height = self.window.winfo_height()
        self.window.attributes("-alpha",0.3)
        # 绑定事件
        self.window.bind("<Key>",self.myquit)
        self.window.bind("<Any-Button>",self.myquit)
        self.window.bind("<Motion>",self.myquit)
        self.canvas = Canvas(self.window,width=self.winth,height=self.height,
                                bg = "#FFFFFF")
        self.canvas.pack()
        for i in range(0,self.ball_nums):
            ball = Ball(self.canvas,scrnwidth=self.winth,scrnheight=self.height)
            ball.creat_canvas()
            self.balls.append(ball)
    def run_screensaver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(20,self.myquit)
    def myquit(self,even):
        self.window.destroy()
def main():
    ScreenSaver()


if __name__=='__main__':
    main()
