import tkinter
window = tkinter.Tk()  # 生成一个窗口
window.title('wtf?')  # 这里写窗体标题
window.geometry('200x300')  # 这里是英文x不是*号
window.resizable(width=True, height=True)  # 手动调整窗口大小是否可用
var1 = tkinter.StringVar()  # tkinter的变量
var1.set('hit it if u dare')  # 设置初始值
on_hit = False
# window.quit() # 退出窗口
# window.update() # 刷新窗口
# ----------------------------标签----------------------------- #
label_test_1 = tkinter.Label(
    window,
    textvariable=var1,
    # fg="blue",
    bg="white",
    font=("Arial", 15),
    height=2,
    width=10,
    justify=tkinter.RIGHT)
# 以上参数：(窗体，字体颜色，背景颜色，字体设置("字体款式,字体大小),标签高度，标签长度，对齐方式（tkinter.LEFT/RIGHT/CENTER）
# 未使用的参数：padx=2(左右两侧的空格数，默认为1),pady=2(上下两侧的空格数，默认为1)
# image=xxx， xxx = tk.PhotoImage(file='路径')
# compound=botton/top/right/left/center 图像位置，文字覆盖图像
label_test_1.pack()  # 设置显示
# ----------------------------按钮------------------------------ #


def hit_it():
    global on_hit  # 使用上述的全局变量
    if on_hit is False:
        on_hit = True
        var1.set('damn son')
    else:
        on_hit = False
        var1.set('')


button_test_1 = tkinter.Button(
    window,
    text="B1",
    height=3,
    width=10,
    fg="blue",
    bg="red",
    activebackground="green",
    command=hit_it)
# activebackground:按钮按下时的背景颜色，activeforeground：按钮按下时的前景字体颜色
# 其他未使用参数：justify,padx,pady
# command=xxx, 按钮执行触发函数
button_test_1.pack()
# --------------------------输入框------------------------------- #
# entry_test_1 = tkinter.Entry(window, width=15, fg="blue", bg="red")
# 其他未使用参数：show="*"(用*代替显示内容), state=readonly/disabled,默认为normal
# entry_test_1.pack()
# --------------------------文本框------------------------------- #
# text_test_1 = tkinter.Text(window)  # 待更新 不会用
# text_test_1.pack()
# --------------------------单选框------------------------------- #
# picked = tkinter.StringVar()
# ratio_button_test_1 = tkinter.Radiobutton(
#    window, text='pick', variable=picked,
#     value='蓝色')  # 这里的variable和value不太明白 # 待更新
# ratio_button_test_1.pack()
# ratio_button_test_2 = tkinter.Radiobutton(
#    window, text='pick', variable=picked, value='红色')
# ratio_button_test_2.pack()
# 未使用：command=xxx
# --------------------------复选框------------------------------- #
# check_button_test_1 = tkinter.Checkbutton(
#     window, text='???')  # 同样variable不明 # 待更新
# heck_button_test_1.pack()
# check_button_test_2 = tkinter.Checkbutton(window, text='!!!')
# check_button_test_2.pack()
# onvalue=1 offvalue=0 选中/未选中时变量的值，分别可以自行设置,command=xxx

# -------------------------- ------------------------------- # # Listbox, Scrollbar待更新, frame框架
# --------------------------pack()------------------------------- #
# pack() fill=X/Y/BOTHNE向方向填充, expand=YES填充剩余空间, side=LEFT/RIGHT/TOP/BOTTOM, ipadx,ipady= , padx=,pady=, anchor=N/S/W/E/NW,NE,SW,SE,CENTER ipadx,padx anchor待实验
# --------------------------grid()------------------------------- #
# --------------------------messagebox()------------------------- #
# --------------------------------------------------------------- #
window.mainloop()  # 必须放在最后
