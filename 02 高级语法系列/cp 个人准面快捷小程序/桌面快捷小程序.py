import tkinter as tk
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
calcu_Button = tk.Button(canvas,image=calcu_img)
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
