import tkinter as tk

# 计算器功能
def calculator():

    def clear():
        cal_enter_input.delete(0,tk.END)
        cal_enter_res.delete(0,tk.END)
    # 计算长度设置
    def calculation(nun):
        list_nun=[1,2,3,4,5,6,7,8,9,0]
        inp=[]
        content = get_enter.get()
        if nun in str(list_nun):
            content = content+nun
            get_enter.set(content)



    cal_root = tk.Toplevel(window)
    cal_root.title("私人订制计算器")
    cal_root.winfo_screenmmwidth()
    cal_root.winfo_screenheight()
    cal_root.geometry("280x360")
    cal_root.resizable(width=False,height=False)
    # 计算器主界面
    cal_canvas = tk.Canvas(cal_root,width=280,height=360)
    cal_img = tk.PhotoImage(file="计算器背景.gif")
    cal_canvas.create_image(140,180,image=cal_img)
    cal_canvas.pack()

    # 计算器的按钮和显示框
    ## 输入框
    get_enter = tk.StringVar()
    get_enter.set(0)
    cal_enter_input= tk.Entry(cal_root,textvariable=get_enter,font="微软雅黑")
    cal_enter_input.pack()
    cal_canvas.create_window(140,30,height=30,width=220,window=cal_enter_input)
    ##结果框
    get_res = tk.StringVar()
    get_res.set(0)
    cal_enter_res=tk.Entry(cal_root,textvariable=get_res,font="微软雅黑")
    cal_enter_res.pack()
    cal_canvas.create_window(140,70,height=30,width=220,window=cal_enter_res)

    # 按键区域容器
    cal_frame = tk.Frame(cal_root)
    cal_frame.pack()
    # 按键区域
    but_c = tk.Button(cal_frame,text="C",width=4,height=1,
                      font="微软雅黑",command=clear)
    but_c.place(x=10,y=10)
    but_d = tk.Button(cal_frame,text="÷",width=4,height=1,
                      font="微软雅黑",command=lambda: calculation("÷"))
    but_d.place(x=60,y=10)
    but_b=tk.Button(cal_frame,text="×",width=4,height=1,
                    font="微软雅黑",command=lambda: calculation("×"))
    but_b.place(x=110,y=10)
    but_r=tk.Button(cal_frame,text="－",width=4,height=1,
                    font="微软雅黑",command=lambda: calculation("－"))
    but_r.place(x=160,y=10)

    but_7 = tk.Button(cal_frame,text="7",width=4,height=1,font="微软雅黑",command=lambda: calculation("7")).place(x=10,y=60)
    but_4 = tk.Button(cal_frame,text="4",width=4,height=1,font="微软雅黑",command=lambda: calculation("4")).place(x=10,y=110)
    but_1 = tk.Button(cal_frame,text="1",width=4,height=1,font="微软雅黑",command=lambda: calculation("1")).place(x=10,y=160)
    but_0 = tk.Button(cal_frame,text="0",width=8,height=1,font="微软雅黑",command=lambda: calculation("0")).place(x=10,y=210)
    but_8 = tk.Button(cal_frame,text="8", width=4,height=1, font="微软雅黑",command=lambda: calculation("8")).place(x=60, y=60)
    but_9 = tk.Button(cal_frame,text="9",width=4,height=1,font="微软雅黑",command=lambda: calculation("9")).place(x=110,y=60)
    but_a = tk.Button(cal_frame,text="＋",width=4,height=3,font="微软雅黑",command=lambda: calculation("＋")).place(x=160,y=68)
    but_5 = tk.Button(cal_frame,text="5",width=4,height=1,font="微软雅黑",command=lambda: calculation("5")).place(x=60,y=110)
    but_6 = tk.Button(cal_frame,text="6",width=4,height=1,font="微软雅黑",command=lambda: calculation("6")).place(x=110,y=110)
    but_2 = tk.Button(cal_frame, text="2", width=4, height=1, font="微软雅黑",command=lambda: calculation("2")).place(x=60, y=160)
    but_3 = tk.Button(cal_frame, text="3", width=4, height=1, font="微软雅黑",command=lambda: calculation("3")).place(x=110, y=160)
    but_f = tk.Button(cal_frame, text="·", width=4, height=1, font="微软雅黑",command=lambda: calculation("·")).place(x=110, y=210)
    but_e = tk.Button(cal_frame, text="＝", width=4, height=3, font="微软雅黑",command=lambda: calculation("＝")).place(x=160, y=170)

    cal_canvas.create_window(140,220,width=230,height=250,window=cal_frame)

    cal_root.mainloop()



# 图形界面框架结构
window = tk.Tk()
window.title("鹏程万里")
window.resizable(width=False,height=False)
window.geometry("280x360")
window.winfo_screenheight()
window.winfo_screenmmwidth()# 取消边框

#主页显示画布背景
canvas = tk.Canvas(window,width=280,height=360)
main_img = tk.PhotoImage(file="主页.gif")
canvas.create_image(140,180,image=main_img)
canvas.pack()

#计算器图标
calcu_img = tk.PhotoImage(file="计算器.gif")
calcu_Button = tk.Button(canvas,image=calcu_img,command=calculator)
calcu_Button.pack()
canvas.create_window(35,40,height=60,width=60,window=calcu_Button)

#记事本图标
note_img = tk.PhotoImage(file="记事本.gif")
note_Button = tk.Button(canvas,image=note_img)
note_Button.pack()
canvas.create_window(100,40,height=60,width=60,window=note_Button)

# 邮件
email_img = tk.PhotoImage(file="邮件.gif")
email_Button = tk.Button(canvas,image=email_img)
email_Button.pack()
canvas.create_window(170,40,height=60,width=60,window=email_Button)
window.mainloop()
