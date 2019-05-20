import tkinter


if __name__ == '__main__':

    window = tkinter.Tk()
    window.title("飞机大战第一版")
    window.resizable(width=False,height=False)

    canvas = tkinter.Canvas(window,width=480,height=600)
    canvas.pack()
    bg_img = tkinter.PhotoImage(file="../img/background.gif")
    canvas.create_image(240,300,anchor=tkinter.CENTER,image=bg_img,tag="bg")

    bee_img = tkinter.PhotoImage(file="../img/bee.gif")
    canvas.create_image(240,300,anchor=tkinter.CENTER,image=bee_img,tag="bee")

    window.mainloop()

