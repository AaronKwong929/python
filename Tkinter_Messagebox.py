import tkinter
from tkinter import messagebox
# import tkinter.messagebox
window = tkinter.Tk()
window.title('test2')
window.geometry('400x400')
window.resizable(width=True, height=True)


def hit_me():
    # tkinter.messagebox.showinfo(title='Hi!', message='???')
    # tkinter.messagebox.showwarning(title='Hi!', message='no!') # 警告
    # tkinter.messagebox.showerror(title='Hi!', message='???')  # 错误提示窗
    # print(tkinter.messagebox.askquestion(title='!!', message='hhh'))  # 会在终端打印yes/no
    # print(tkinter.messagebox.askyesno(title='!!', message='hhh'))  # True/false
    # print(tkinter.messagebox.askretrycancel(title='!!', message='hhh'))  # 重试，返回True/False
    print(tkinter.messagebox.askyesnocancel(title='!!', message='hhh'))  # Yes/No/None

tkinter.Button(window, height=5, width=10, text='press', command=hit_me).pack()

window.mainloop()