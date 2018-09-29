import tkinter

window = tkinter.Tk()
window.title('test04')
window.geometry('500x400')
window.resizable(width=True, height=True)

content_label = tkinter.Label(window, bg='yellow', width=30, height=5, text='empty')
content_label.pack()

selected_var = tkinter.StringVar()


def print_selection():
    content_label .config(text='you have selected' + selected_var.get())
r1 = tkinter.Radiobutton(window, text='Option A', variable=selected_var, value='A', command=print_selection)
# 将value='A'赋值给selected_var
r1.pack()
r2 = tkinter.Radiobutton(window, text='Option B', variable=selected_var, value='B', command=print_selection)
r2.pack()
r3 = tkinter.Radiobutton(window, text='Option C', variable=selected_var, value='C', command=print_selection)
r3.pack()
window.mainloop()