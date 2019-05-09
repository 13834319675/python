import tkinter as tk

BaseFrame = tk.Tk()

def rog():
    name = e1.get()
    pwd = e2.get()


    if name == "111" or pwd == "222":
        l3["text"]="登陆成功"

    else:
        l3["text"]="账号密码错误"
        e1.delete(0,name)
        e2.delete(0,pwd)


l1 =tk.Label(BaseFrame,text = "登陆: ").grid(row=0,column=0,sticky="w")
e1 =tk.Entry(BaseFrame,show=None)
e1.grid(row=0,column=1,sticky="e")
l2 = tk.Label(BaseFrame,text="密码: ").grid(row=1,column=0,sticky="w")
e2 = tk.Entry(BaseFrame,show="*")
e2.grid(row=1,column=1,sticky="e")
b = tk.Button(BaseFrame,text= "登陆",command=rog).grid(row=2,column=1,sticky ="e")

l3 = tk.Label(BaseFrame,text="")
l3.grid(row=3,column=1,sticky="w")
BaseFrame.mainloop()