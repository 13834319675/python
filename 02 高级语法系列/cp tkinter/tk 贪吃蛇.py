import tkinter
import random

class Food():
    def __init__(self,snk_list):

        self.snk_list = snk_list
        s1 = set(self.snk_list)
        s = canvas_set.difference(s1)

        self.food_list = list(s)
        self.food_point = random.choice(self.food_list)
        """以上表示在蛇和画布像素的差集中随机产生食物的点,并返回"""
        self.make_point()

    def make_point(self):
        return self.make_point()

class Snk():
    '''需要完成的功能：
            1. 控制移动，吃Food
            3. 判断是否撞墙和撞自己，如是则提示结束游戏'''

    def __init__(self,snk_list,food_point,move_x=0,move_y=0):
        '''需要接收的信息：Snk_list,Food_point,移动指令(move_x,move_y 默认值为0)'''
        self.snk_list = snk_list
        self.food_point = food_point
        self.move_x = move_x
        self.move_y = move_y
        # 求出将要移动的点位
        l = len(self.snk_list)
        # 将要移动的点位,等于蛇的第二个像素点的x卓彪加上在x轴上移动的像素点数,同理y
        self.move_pointx = self.snk_list[l-1][0]+(self.move_x+px)
        self.move_pointy = self.snk_list[l-1][1]+(self.move_y+px)
        self.move_point = (self.move_x,move_y) # 坐标以元祖的方式保存

    def Snk_isover(self):#撞自己和撞墙的判断
        if self.move_pointx<0 or self.move_x>=self.canvas_w: #(超出屏幕)
            return True
        elif self.move_pointy<0 or self.move_y>=self.canvas_h:
            return  True
        elif self.move_point in self.snk_list:
            # 注意没有移动指令的时候，移动点是一直在顶端的
            if self.move_x!=0 or self.move_y:
                return True
            else:
                return False
        else:
            return False

    def Snk_move(self):  # 此函数必须要返回Food_point和Snk_list
        # 移动过程中吃的情况,蛇将要运动的方向的坐标和食物的坐标相等
        # 则把将要移动点的坐标也就是食物的坐标放入snk_list中.蛇增加长度
        if self.move_point == self.food_point
            self.snk_list.append(self.move_point)
            # 实例化食物
            i = Food(self.snk_list)
            self.food_point = i.make_point()  # 将随机生成的坐标赋值给食物
            return self.food_point ,self.snk_list

        else:
            if self.move_x != 0 or self.move_y!=0:
                # 有移动指令才执行
                # 蛇的移动就是删除后一个像素增加第一个像素
                self.snk_list.remove(self.snk_list[0])
                self.snk_list.append(self.move_point)
                return self.snk_list,self.food_point
            else:
                return self.snk_list,self.food_point

class Win(tkinter.Tk):#窗口类 继承自tkinter
    '''需要完成的功能：
            1. 创建一个画布，展示Snk,Food
            2. 向Snk发出移动指令(可自动可手动),并接收返回值
            3. 在画布中展示Snk移动，吃Food的效果
            4. Game_over时给出提示，并执行重新开始或退出'''