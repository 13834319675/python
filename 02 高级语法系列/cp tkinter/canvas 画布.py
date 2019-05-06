import tkinter as tk

window = tk.Tk()
window.title("canvas画布示例")
window.geometry("500x300")

canvas = tk.Canvas(window,bg="green", height=200, width=500)
# 设置图片在画布上的位置,载入图片
image_file=tk.PhotoImage(file="4e.png")  # 相对路径
image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处

# 设置四个坐标
x0,x1,y0,y1=100,100,150,150
line = canvas.create_line(x0+50,x1+50,y0+100,y1+100)  # 直线
oval = canvas.create_oval(x0+150,x1+150,y0-20,y1-20)  #  圆
arc = canvas.create_arc(x0,x1,y0,y1,start=0, extent=180) # 扇形从0度到180度
rect = canvas.create_rectangle(250,250,100,100)
canvas.pack()
# 创建一个函数 定义一个长方形的移动事件
def moveit():
    canvas.move(rect,3,3)

b = tk.Button(window,text="rext move",width=20,height=2,font=("微软雅黑",12),command=moveit)
b.pack()

window.mainloop()
