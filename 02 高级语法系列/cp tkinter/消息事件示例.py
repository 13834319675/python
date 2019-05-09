# 事件

import tkinter as tk
def baselabel(event):
    global BaseFrame
    print("点击")
    tk.Label(BaseFrame,text="我被点击了").pack()


BaseFrame = tk.Tk()
l = tk.Label(BaseFrame,text="点我")
l.bind("<Button-1>",baselabel)
l.pack()

BaseFrame.mainloop()


