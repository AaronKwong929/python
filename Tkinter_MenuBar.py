import tkinter

window = tkinter.Tk()
window.title('test04')
window.geometry('500x400')
window.resizable(width=True, height=True)

counter = 0
label_1 = tkinter.Label(window, text='', bg='yellow', width=20, height=5)
label_1.pack()


def New1():
    global counter
    label_1.config(text='do' + str(counter))
    counter += 1


menubar_1 = tkinter.Menu(window)  # 创建一个菜单栏

filemenu = tkinter.Menu(menubar_1, tearoff=False,)  #tearoff=True 顶上有一条虚线，False没有
menubar_1.add_cascade(label='File', menu=filemenu)  # 对菜单进行操作
filemenu.add_command(label='New', command=New1)
filemenu.add_command(label='Open', command=New1)
filemenu.add_command(label='Save', command=New1)
filemenu.add_separator()  # 分割线
filemenu.add_command(label='Exit', command=window.quit)


editmenu = tkinter.Menu(menubar_1, tearoff=False,)
menubar_1.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=New1)
editmenu.add_command(label='Copy', command=New1)
editmenu.add_command(label='Paste', command=New1)


submenu = tkinter.Menu(filemenu, tearoff=False)  # 在哪个对象中创建子菜单
filemenu.add_cascade(label='Import', menu=submenu,underline=0)
submenu.add_command(label='Submenu1', command=New1)
window.config(menu=menubar_1)  # 相当于pack()
window.mainloop()