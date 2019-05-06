# menu菜单

import tkinter as tk

window = tk.Tk()
window.title("menu菜单")
window.geometry("500x300")

l = tk.Label(window, text='      ', bg='green')
l.pack()

# 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0


def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1


# 创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
# 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label="New",command=do_job)
filemenu.add_command(label="Open",command=do_job)
filemenu.add_command(label="Save",command=do_job)
# 插入分割线
filemenu.add_separator()
filemenu.add_command(label="Exit",command=do_job)
# 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=do_job)
editmenu.add_command(label="Copy",command=do_job)
editmenu.add_command(label="Paste",command=do_job)
# 创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu,tearoff=0) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
# 给放入的菜单submenu命名为Import
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="submenu1",command=do_job)
# 穿件一个help菜单
helpmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="find",command=do_job)
# 创建菜单栏完成后，配置让菜单栏menubar显示出来
window.config(menu=menubar)
window.mainloop()

