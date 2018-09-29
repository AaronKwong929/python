import tkinter

window = tkinter.Tk()
window.title('test04')
window.geometry('500x400')
window.resizable(width=True, height=True)


def print_selection(v):  # 这里有参数v
    scale_label.config(text='you have selected:' + v)


scale_label = tkinter.Label(window, bg='yellow', width=20, text='empty')
scale_label.pack()

scale_item = tkinter.Scale(
    window,
    label='try it',
    from_=0,
    to=10,
    orient=tkinter.HORIZONTAL,  # or VERTICAL垂直
    length=300,  # Scale长度，单位为像素
    showvalue=True,  # 比例尺当前位置
    tickinterval=2,  # Scale刻度
    resolution=0.1,  # 精度控制
    command=print_selection)  # length单位像素
scale_item.pack()
window.mainloop()