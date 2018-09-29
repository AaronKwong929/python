import tkinter
window = tkinter.Tk()
window.title('test3')
window.geometry('600x400')
window.resizable(width=True, height=True)

var1 = tkinter.StringVar()

label = tkinter.Label(window, bg='yellow', width=10, textvariable=var1)
label.pack()


def print_selection():
    value = listbox1.get(listbox1.curselection())
    var1.set(value)


button1 = tkinter.Button(
    window,
    text='print selection',
    width=15,
    height=2,
    command=print_selection)
button1.pack()

var2 = tkinter.StringVar()
var2.set((11, 12, 13, 14, 15))  # 设置一个元祖

listbox1 = tkinter.Listbox(window, listvariable=var2)  # 设置listbox时把元祖也设置进去
list_items = [1, 2, 3, 4]  # 设置一个列表
for item in list_items:
    listbox1.insert('end', item)  # listbox末尾插入列表
listbox1.insert(1, 'first')  # 索引插入
listbox1.insert(3, 'second')
# listbox1.delete(2)  # 索引删除
listbox1.pack()


def delete_all():
    listbox1.delete(0, 'end')


delete_all_button = tkinter.Button(
    window, text='删除所有内容', width=15, height=2, command=delete_all)
delete_all_button.pack()

var3 = tkinter.StringVar()
add_entry = tkinter.Entry(window, width=10, bg='yellow')
add_entry.pack()


def get_data():
    var3 = add_entry.get()
    listbox1.insert('end', var3)
    # add_entry.selection_clear() （未实现，输入文本后清空输入框）


add_item_button = tkinter.Button(
    window, text='添加内容', width=15, height=2, command=get_data)
add_item_button.pack()


def delete_data():
    listbox1.delete(listbox1.curselection())


delete_item_button = tkinter.Button(
    window, text='删除选中内容', width=15, height=2, command=delete_data)
delete_item_button.pack()
window.mainloop()

# 添加一个按钮用以向文本框添加内容  # （已实现）
# 添加一个按钮用以删除选中内容  # （已实现）
# 添加一个按钮用以删除全部内容listbox1.insert(0,END)  #（已实现）