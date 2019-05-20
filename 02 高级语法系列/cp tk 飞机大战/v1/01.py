import tkinter

root_window = tkinter.Tk()
root_window.title("盖世大战")
# 固定窗口大小
root_window.resizable(width=False, height=False)

window_canvas = tkinter.Canvas(root_window,
                               width=480,
                               height=650)
window_canvas.pack()

# 记录当前位置
now_x, now_y = 260, 550
# 移动速度与方向
x, y = 0, 0


def move_up(self):
    global x, y
    x = 0
    y = -1


def move_down(self):
    global x, y
    x = 0
    y = 1


def move_left(self):
    global x, y
    x = -1
    y = 0


def move_right(self):
    global x, y
    x = 1
    y = 0


# 绑定方向键
root_window.bind('w', move_up)
root_window.bind('s', move_down)
root_window.bind('a', move_left)
root_window.bind('d', move_right)

bullet = tkinter.PhotoImage(file="./feiji/zidan.gif")


# 英雄移动
def hero_move():
    global x, y
    window_canvas.move("hero", x, y)
    global now_x, now_y
    now_x += x
    now_y += y
    window_canvas.after(10, hero_move)


# 移动子弹
def biu_move():
    window_canvas.move("bullet", 0, -3)
    window_canvas.after(20, biu_move)


# 制造子弹
def biu(self):
    global now_y
    for i in range(1, 12):  # 制造一排子弹
        window_canvas.create_image(i * 40 + now_x - 240, now_y - 30, image=bullet, tags='bullet')
                                    #设置子弹的宽度和位置

root_window.bind('j', biu)  # 按J发射


def main():
    back = tkinter.PhotoImage(file="./feiji/background.gif")  # 只有png和gif可以
    window_canvas.create_image(260, 350, image=back)
    # 制造英雄
    hero = tkinter.PhotoImage(file="./feiji/hero.gif")
    window_canvas.create_image(260, 550, image=hero, tags='hero')
    biu_move()
    hero_move()
    tkinter.mainloop()


if __name__ == '__main__':
    main()

