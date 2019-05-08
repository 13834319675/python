import tkinter as tk
import tkinter.messagebox
import pickle

window=tk.Tk()
window.title("登陆")
window.geometry("600x400")

canva = tk.Canvas(window,width=400,height=200,bg="red")
image_file = tk.PhotoImage(file="4e.png")
image = canva.create_image(200,0,anchor="n",image=image_file)
canva.pack(side="top")

l = tk.Label(window,text="欢  迎",font=("Arial",16),height=2).pack()

fram = tk.Frame(window).pack()
fram_user = tk.Frame(fram).pack(side="left")
fram_pass = tk.Frame(fram).pack(side="right")

tk.Label(fram_user,text="用户名:",font=("微软雅黑",13)).place(x=110,y=253)
tk.Label(fram_pass,text="密   码:",font=("微软雅黑",13)).place(x=110,y=278)
# 接口
var_use_name=tk.StringVar()
var_use_name.set("我是谁?我在哪?我要干嘛?")
e1=tk.Entry(fram_user,textvariable=var_use_name,show=None,width=30)
e1.pack()
var_use_pass=tk.StringVar()
e2=tk.Entry(fram_pass,textvariable=var_use_pass,show="*",width=30)
e2.pack()

# 建立三个函数 分别实现登陆注册和重置的功能
def user_login():
    user_name=var_use_name.get()
    user_pass=var_use_pass.get()
    # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    # 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open("us_pa_file.pickle","rb") as f:
            user_info=pickle.load(f)
    except FileNotFoundError:
# 这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
# 的用户和密码写入，即用户名为`admin`密码为`admin`
        with open("us_pa_file.pickle","wb") as f:
            user_info={"admin":"admin"}
            pickle.dump(user_info,f)
            f.close()
    # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
    if user_name in user_info:
        if user_pass==user_info[user_name]:
            tkinter.messagebox.showinfo(title="欢迎",message="账号({})登陆成功 how are you?".format(user_name))
        else:
            tkinter.messagebox.showerror(title="提示", message="账号({})密码错误".format(user_name))
    else:
        is_set_up=tkinter.messagebox.askyesno(title="提示",message="输入的账号({})不存在,是否注册?".format(user_name))
        if is_set_up:
            set_up()

def set_up():
    def sign_to_set_up():
        # 以下获取三个输入框的内容
        nn = var_new_name
        np = var_new_pass
        fp = var_firm_pass

        with open("us_pa_file.pickle", "rb") as user_file:
            exist_user_info = pickle.load(user_file)

        # 判断两次密码不一样,则提示错误
        if np != fp:
            tkinter.messagebox.showerror(title="错误",message="两次输入的密码不一样")
        # 如果用户名存在,则提示已存在
        if nn in exist_user_info:
            tkinter.messagebox.showerror(title="提示",message="用户名已存在")
        else:
            exist_user_info[nn]=np
            with open("us_pa_file.pickle","wb") as user_file:
                pickle.dump(exist_user_info,user_file)
                user_file.close()
            tkinter.messagebox.showinfo(title="提示",message="保存成功")
            window_set_up.destroy() # 销毁窗口

    window_set_up = tk.Toplevel(window)
    window_set_up.title("注册")
    window_set_up.geometry("300x200")

    tk.Label(window_set_up,text="新账号").place(x=10,y=10)
    var_new_name=tk.StringVar()
    var_new_name.set("新账号")
    set_up_entry1 = tk.Entry(window_set_up,show=None,textvariable=var_new_name)
    set_up_entry1.place(x=130,y=10)

    tk.Label(window_set_up,text="新密码").place(x=10,y=50)
    var_new_pass=tk.StringVar()
    set_up_entry2 = tk.Entry(window_set_up,show="*",textvariable=var_new_pass)
    set_up_entry2.place(x=130,y=50)

    tk.Label(window_set_up,text="确认密码").place(x=10,y=90)
    var_firm_pass = tk.StringVar()
    set_up_entry3 = tk.Entry(window_set_up,show="*",textvariable=var_firm_pass)
    set_up_entry3.place(x=130,y=90)

    tk.Button(window_set_up,text="注册",command=sign_to_set_up).place(x=180,y=120)

def del_all_eny():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)


# 登陆和注册和重置按钮
b_login=tk.Button(window,text="登陆",font=("微软雅黑",10),command=user_login).place(x=200,y=320)
b_steup=tk.Button(window,text="注册",font=("微软雅黑",10),command=set_up).place(x=280,y=320)
b_search=tk.Button(window,text="重置",font=("微软雅黑",10),command=del_all_eny).place(x=360,y=320)
window.mainloop()
