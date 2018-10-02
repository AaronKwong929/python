import tkinter

window = tkinter.Tk()
window.title('test04')
window.geometry('500x400')
window.resizable(width=True, height=True)

canvas = tkinter.Canvas(window, bg='yellow', height=400, width=400)
canvas.pack()
# image_1 = tkinter.PhotoImage(file='')  # 添加图片
# image = canvas.create_image(0, 0, anchor='', image=image_1)  # anchor='NW/ N/ NE/ W/ E/ CENTER/ SW/ S/ SE
x0, y0, x1, y1, x2, y2, x3, y3, x4, y4 = 50, 50, 80, 80, 120, 170, 220, 270, 160, 170

oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  # 椭圆
line = canvas.create_line(x0, y0, x1, y1)  # 直线  # 先后位置影响覆盖
arc = canvas.create_arc(
    x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=270)  # 扇形 从0-180°
rect = canvas.create_rectangle(100, 30, 120, 50)  # 正方形
polygon = canvas.create_polygon(x0, y0, x1, y1, x2, y2)  # 多边形


def move_it():
    canvas.move(rect, 2, 0)  # (canvas对象， x方向， y方向)(单位为像素)


button = tkinter.Button(window, text='move', command=move_it).pack()

window.mainloop()