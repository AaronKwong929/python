import tkinter
window = tkinter.Tk()
window.title('test2')
window.geometry('400x400')
'''
tkinter.Label(window, text='11111').pack(side='top')
tkinter.Label(window, text='22222').pack(side='bottom')
tkinter.Label(window, text='33333').pack(side='left')
tkinter.Label(window, text='44444').pack(side='right')
'''
#-------------------------------grid和pack要单独使用---------------------------------#
'''
for i in range(4):
    for j in range(4):
        tkinter.Label(window, text=666).grid(row=i, column=j, ipadx=10, ipady=10)  # pad x/y 内部扩展  ipad x/y
'''
#-----------------------------------------------------------------------------------#
tkinter.Label(window, text=666).place(x=0, y=100)  # 所以anchor究竟什么作用
window.mainloop()