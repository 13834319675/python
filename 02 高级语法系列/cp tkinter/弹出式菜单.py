import tkinter as tk

BaseFrame = tk.Tk()

def makelabel():
    global BaseFrame
    tk.Label(BaseFrame,text="吃喝拉撒睡=快乐").pack()

menus = tk.Menu(BaseFrame,tearoff=0)

for x in ["吃","喝","拉","撒"]:
    menus.add_separator()
    menus.add_command(label=x)
# 事件处理函数一定要至少有一个参数，且第一个参数表示的是系统事件

menus.add_command(label="睡",command=makelabel)

def pop(event):
    # 注意使用 event.x 和 event.x_root的区别
    # menubar.post(event.x_root, event.y_root)
    menus.post(event.x_root,event.y_root)




BaseFrame.bind("<Button-3>",pop)
BaseFrame.mainloop()