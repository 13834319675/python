import tkinter
import random

'''
构成：运行窗口Win，需要展现的Snk(snake)，被吃的食物Food
具体成分：
    1. Win：将效果展示在画板(canvas)上，将canvas分成若干个像素格 
    2. Snk：由连续的象素格组成，可控制移动，可自动移动，可吃食物Food，每次移动一个像素格
    3. Food：在canvas和Snk的差集中，随机生产一个像素格
运行思路：win--控制-->Snk--控制-->Food

'''

'''
画板的长宽(canvas_w,canvas_h)和像素点集合(canvas_set),像素大小(px)作为全局变量.
目的：减少传入参数的个数
'''


class Food():
    '''
    需要完成的功能：调用一次自动生成一个象素格(点坐标)，并返回坐标点
    '''

    def __init__(self, Snk_list):
        '''
        需要接收的信息：Snk的像素点(Snk_list)
        '''
        self.Snk_list = Snk_list

        s1 = set(self.Snk_list)
        s = canvas_set.difference(s1)

        self.Food_list = list(s)
        self.Food_point = random.choice(self.Food_list)  # 随机生成Food点

        self.make_point()

    def make_point(self):  # 注意：__init__() 貌似返回不了数据类型的值
        return self.Food_point


class Snk():
    '''
    需要完成的功能：
        1. 控制移动，吃Food
        3. 判断是否撞墙和撞自己，如是则提示结束游戏
    '''

    def __init__(self, Snk_list, Food_point, move_x=0, move_y=0):
        '''
        需要接收的信息：Snk_list,Food_point,移动指令(move_x,move_y 默认值为0)
        '''
        self.Snk_list = Snk_list
        self.Food_point = Food_point
        self.move_x = move_x
        self.move_y = move_y

        # 求出将要移动到达的点位
        l = len(self.Snk_list)
        self.move_pointx = self.Snk_list[l - 1][0] + (self.move_x * px)
        self.move_pointy = self.Snk_list[l - 1][1] + (self.move_y * px)
        self.move_point = (self.move_pointx, self.move_pointy)
        # 注意：坐标点以元组的方式保存

    def Snk_isover(self):
        # 进行撞墙和撞自己的判断
        if self.move_pointx < 0 or self.move_pointx >= canvas_w:
            return True
        elif self.move_pointy < 0 or self.move_pointy >= canvas_h:
            return True
        elif self.move_point in self.Snk_list:
            # 注意没有移动指令的时候，移动点是一直在顶端的
            if self.move_x != 0 or self.move_y != 0:
                return True
            else:
                return False
        else:
            return False

    def Snk_move(self):  # 此函数必须要返回Food_point和Snk_list

        if self.move_point == self.Food_point:
            self.Snk_list.append(self.move_point)
            i = Food(self.Snk_list)
            self.Food_point = i.make_point()
            return self.Food_point, self.Snk_list

        else:
            if self.move_x != 0 or self.move_y != 0:
                # 有移动指令才执行
                self.Snk_list.remove(self.Snk_list[0])
                self.Snk_list.append(self.move_point)
                return self.Food_point, self.Snk_list
            else:
                return self.Food_point, self.Snk_list


class Win(tkinter.Tk):
    '''
    需要完成的功能：
        1. 创建一个画布，展示Snk,Food
        2. 向Snk发出移动指令(可自动可手动),并接收返回值
        3. 在画布中展示Snk移动，吃Food的效果
        4. Game_over时给出提示，并执行重新开始或退出
    '''

    def __init__(self, a=500, b=600, c=20):
        # 先对画板长宽像素数据进行处理
        global px
        px = int(c)
        w = int(a)
        h = int(b)
        w = w // px
        h = h // px
        global canvas_w
        canvas_w = w * px
        global canvas_h
        canvas_h = h * px

        # 像素点的集合
        canvas_list = list()
        for i in range(1, w):
            for j in range(1, h):  # 注意：点坐标必须要元组，不然无法转集合
                canvas_list.append((i * px, j * px))
        global canvas_set
        canvas_set = set(canvas_list)

        # 创建画板
        tkinter.Tk.__init__(self)
        self.canvas = tkinter.Canvas(self, width=canvas_w, height=canvas_h, bg='gray')
        self.canvas.grid(row=2)

        # 创建初始Snk
        self.Snk_list = list()
        # 点1
        x1 = (w // 2) * px
        y1 = (h // 2) * px
        p1 = (x1, y1)
        # 点2
        x2 = (w // 2) * px + px
        y2 = (h // 2) * px
        p2 = (x2, y2)
        # 点3
        x3 = (w // 2) * px + px * 2
        y3 = (h // 2) * px
        p3 = (x3, y3)
        self.Snk_list.append(p1)
        self.Snk_list.append(p2)
        self.Snk_list.append(p3)
        self.Snk = self.canvas.create_line(self.Snk_list, fill='green', width=px)

        # 创建初始Food
        i = Food(self.Snk_list)
        self.Food_point = i.make_point()
        self.Food = self.canvas.create_rectangle(self.Food_point[0] - px // 2, self.Food_point[1] - px // 2,
                                                 self.Food_point[0] + px // 2, self.Food_point[1] + px // 2,
                                                 fill='red', outline='green')

        # 初始跑动
        self.run()
        self.automatic_run()

        # 接收移动指令
        self.bind('<Key-Up>', self.move_up)
        self.bind('<Key-Down>', self.move_down)
        self.bind('<Key-Left>', self.move_left)
        self.bind('<Key-Right>', self.move_right)

        self.mainloop()

    def run(self, move_x=0, move_y=0):  # 主运行程序

        i = Snk(self.Snk_list, self.Food_point, move_x, move_y)
        isover = i.Snk_isover()
        self.Food_point, self.Snk_list = i.Snk_move()
        # 进行判断
        if isover == False:  # 删除原来的Snk和Food，生成新的Snk和Food
            self.canvas.delete(self.Snk)
            self.Snk = self.canvas.create_line(self.Snk_list, fill='green', width=px)

            self.canvas.delete(self.Food)
            self.Food = self.canvas.create_rectangle(self.Food_point[0] - px // 2, self.Food_point[1] - px // 2,
                                                     self.Food_point[0] + px // 2, self.Food_point[1] + px // 2,
                                                     fill='red', outline='green')
        else:
            self.game_over()

    # 移动指令的执行
    def move_up(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][1] == self.Snk_list[ls - 2][1]:
            self.run(0, -1)
        else:
            if self.Snk_list[ls - 1][1] < self.Snk_list[ls - 2][1]:
                self.run(0, -1)
            else:
                self.run(0, 0)

    def move_down(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][1] == self.Snk_list[ls - 2][1]:
            self.run(0, 1)
        else:
            if self.Snk_list[ls - 1][1] > self.Snk_list[ls - 2][1]:
                self.run(0, 1)
            else:
                self.run(0, 0)

    def move_left(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][0] == self.Snk_list[ls - 2][0]:
            self.run(-1, 0)
        else:
            if self.Snk_list[ls - 1][0] < self.Snk_list[ls - 2][0]:
                self.run(-1, 0)
            else:
                self.run(0, 0)

    def move_right(self, event):
        ls = len(self.Snk_list)
        if self.Snk_list[ls - 1][0] == self.Snk_list[ls - 2][0]:
            self.run(1, 0)
        else:
            if self.Snk_list[ls - 1][0] > self.Snk_list[ls - 2][0]:
                self.run(1, 0)
            else:
                self.run(0, 0)

    # 自动跑动程序
    def automatic_run(self):
        ls = len(self.Snk_list)

        if self.Snk_list[ls - 1][0] == self.Snk_list[ls - 2][0]:
            if self.Snk_list[ls - 1][1] > self.Snk_list[ls - 2][1]:
                self.run(0, 1)
            else:
                self.run(0, -1)

        else:
            if self.Snk_list[ls - 1][0] > self.Snk_list[ls - 2][0]:
                self.run(1, 0)
            else:
                self.run(-1, 0)

        self.canvas.after(500, self.automatic_run)

    # 提示结束
    def game_over(self):
        self.canvas.create_text((canvas_w // 2), (canvas_h // 2), text='Game Over', font=70)
        qb = tkinter.Button(self, text='Quit', font=50, command=self.destroy)
        qb.grid(row=0)
        rb = tkinter.Button(self, text='Again', font=50, command=self.again)
        rb.grid(row=1)

    # 重新开始
    def again(self):
        self.destroy()
        self.__init__()


if __name__ == '__main__':  # 程序运行入口

    win = Win(500, 600, 20)