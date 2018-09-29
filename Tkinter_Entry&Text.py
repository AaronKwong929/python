import tkinter
window = tkinter.Tk()
window.title('test2')
window.geometry('400x400')
window.resizable(width=True, height=True)
entry = tkinter.Entry(window)
entry.pack()
# 宽度width=1， fg='blue'字显示颜色,bg='red'背景色，show='*'用符号代替文本, state=readonly/disabled,默认为normal


def insert_point():
    var = entry1.get()
    text1.insert('insert', var)  # 'insert'可以改为坐标值1.0(第一行第0位)


def insert_end():
    var = entry1.get()
    text1.insert('end', var)

def delete_all_content():
    text1.delete(1.0, 'end')  # 这个1.0不明觉厉


cursor_insert_button = tkinter.Button(window, text='根据光标位置插入', width=15, height=2, command=insert_point)
cursor_insert_button.pack()
end_insert_button = tkinter.Button(window, text='末尾插入', width=15, height=2, command=insert_end)
end_insert_button.pack()
delete_all_button = tkinter.Button(window, text='清空文本框', width=15, height=2, command=delete_all_content)
delete_all_button.pack()
content = tkinter.Text(window, width=30, height=10)
content.pack()

window.mainloop()