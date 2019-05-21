import tkinter as tk

def hero_move(event): # 英雄机的移动
    if event.keysym=="Up":
        canvas.move(2,0,-8)
    if event.keysym=="Down":
        canvas.move(2,0,8)
    if event.keysym=="Left":
        canvas.move(2,-8,0)
    if event.keysym=="Right":
        canvas.move(2,8,0)

def bul_move(event):
    canvas.move("bull",0,3)
    canvas.after(20,bul_move)

root = tk.Tk()
root.title("飞机大战第二版")
root.resizable(width=False,height=False)
canvas = tk.Canvas(root,width=480,height=600)
canvas.pack()
bg_img = tk.PhotoImage(file="../img/background.gif")
canvas.create_image(240,300,anchor="center",image=bg_img,tag="bg")
hero_img = tk.PhotoImage(file="../img/hero.gif")
canvas.create_image(240,500,image=hero_img,tag="hero")
bull_img=tk.PhotoImage(file="../img/bullet.gif")
canvas.create_image(240,440,image=bull_img,tag="bull")
canvas.bind_all("<KeyPress-Up>",hero_move)
canvas.bind_all("<KeyPress-Down>",hero_move)
canvas.bind_all("<KeyPress-Left>",hero_move)
canvas.bind_all("<KeyPress-Right>",hero_move)
root.mainloop()

