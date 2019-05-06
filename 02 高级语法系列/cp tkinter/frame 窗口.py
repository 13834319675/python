import tkinter as tk
window=tk.Tk()
window.title("frame窗口")
window.geometry("500x300")

l = tk.Label(window,text="on the window",bg = "red",font=("Arial",16)).pack()
fram = tk.Frame(window).pack()

fram_l=tk.Frame(fram).pack(side="left")
fram_r=tk.Frame(fram).pack(side="right")
# 创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识

tk.Label(fram_l, text='on the frame_l1', bg='green').pack()
tk.Label(fram_l, text='on the frame_l2', bg='green').pack()
tk.Label(fram_l, text='on the frame_l3', bg='green').pack()
tk.Label(fram_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(fram_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(fram_r, text='on the frame_r3', bg='yellow').pack()

# 第8步，主窗口循环显示
window.mainloop()