# pack布局
import tkinter as tk

BaseFrame = tk.Tk()
but1 = tk.Button(BaseFrame,text="A")
but1.pack(side = "left",expand=tk.YES,fill=tk.Y)

but2 = tk.Button(BaseFrame,text="B")
but2.pack(side = "right",expand=tk.YES,fill=tk.BOTH)

but2 = tk.Button(BaseFrame,text="C")
but2.pack(side=tk.RIGHT,expand=tk.YES,fill=tk.BOTH,anchor=tk.NE)

but2 = tk.Button(BaseFrame,text="D")
but2.pack(side=tk.LEFT,expand=tk.NO,fill=tk.Y)

btn2 = tk.Button(BaseFrame, text='E')
btn2.pack(side=tk.TOP, expand=tk.NO, fill=tk.BOTH)

but3 = tk.Button(BaseFrame,text="F")
but3.pack(side="bottom",expand="yes")

but2 = tk.Button(BaseFrame,text="G")
but2.pack(anchor="se")
BaseFrame.mainloop()

