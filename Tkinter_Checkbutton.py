import tkinter

window = tkinter.Tk()
window.title('test04')
window.geometry('500x400')
window.resizable(width=True, height=True)

label = tkinter.Label(window, bg='yellow', width=20, text='empty')
label.pack()


def print_content():
    if (var1.get() == 1) & (var2.get() == 0):
        label.config(text='I love Python only.')
    elif (var1.get() == 0) & (var2.get() == 1):  # 写成if会导致只选一个会显示else内容，要写成elif
        label.config(text='I love C++ only.')
    elif (var1.get() == 1) & (var2.get() == 1):
        label.config(text='I love both.')
    else:
        label.config(text='I love neither of them.')
    


var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
checkbutton_1 = tkinter.Checkbutton(
    window,
    text='Python',
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=print_content)
checkbutton_1.pack()
checkbutton_2 = tkinter.Checkbutton(
    window,
    text='C++',
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=print_content)
checkbutton_2.pack()
window.mainloop()