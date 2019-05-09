# grid佈局

import tkinter as tk

BaseFrame = tk.Tk()

#下面被注释掉的一行代码跟下面两行代码等效
lb1 = tk.Label(BaseFrame,text="账号:").grid(row=0,column=0,sticky="w")
e1 = tk.Entry(BaseFrame,show=None).grid(row=0,column=1,sticky="e")

lb2 = tk.Label(BaseFrame,text="密码:").grid(row=1,column=0,sticky="w")
e2 = tk.Entry(BaseFrame,show="*").grid(row=1,column=1,sticky="e")

b = tk.Button(BaseFrame,text="登陆").grid(row=3,column=1,sticky="e")
BaseFrame.mainloop()