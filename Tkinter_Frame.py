import tkinter
window = tkinter.Tk()
window.title('test2')
window.geometry('400x400')
window.resizable(width=True, height=True)

tkinter.Label(window, text='on the window').pack()
frm = tkinter.Frame(window)
frm.pack()
frm_left = tkinter.Frame(frm, )
frm_right = tkinter.Frame(frm, )
frm_left.pack(side='left')
frm_right.pack(side='right')

tkinter.Label(frm_left, text='on frm_left').pack()
tkinter.Label(frm_left, text='on frm_left(2)').pack()
tkinter.Label(frm_right, text='on frm_right').pack()
window.mainloop()