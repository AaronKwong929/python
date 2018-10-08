import tkinter
from tkinter import messagebox
import pickle
import re

window = tkinter.Tk()
window.title('实例1：实现登录窗口')
window.geometry('400x400')

var_user_name = tkinter.StringVar()
var_password = tkinter.StringVar()
tkinter.Label(window, text='User name:', width=10, height=2).place(x=50, y=260)
tkinter.Label(window, text='Password:', width=10, height=2).place(x=50, y=310)
username_entry = tkinter.Entry(window, width=20, textvariable=var_user_name).place(x=130, y=270)
password_entry = tkinter.Entry(window, width=20, textvariable=var_password, show='*').place(x=130, y=320)

canvas1 =tkinter.Canvas(window)
image_file = tkinter.PhotoImage(file='C:\\Python\\python\\timg.gif')
image = canvas1.create_image(0, 0,anchor='nw', image=image_file)  # anchor锚定图片西北顶点在0，0点处
canvas1.pack()

def user_login():  # 登录按钮触发
    user_name = var_user_name.get()  # 获取entry内参数
    user_password = var_password.get()
    try:
        with open('user_info.pickle', 'rb') as user_file:  # pickle模块
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle', 'wb')as user_file:
            user_info={'admin': 'admin'}
            pickle.dump(user_info, user_file)
    if user_name == '' or user_password == '':  # 没有输入内容
        tkinter.messagebox.showerror(title='Eroor', message='Wrong input. Please try again.')
    elif user_name in user_info:  # 用户名存在
        if user_password == user_info[user_name]:  # 密码正确，登陆成功
            tkinter.messagebox.showinfo(title='Welcome', message='You have now signed in.' + user_name)
        else:  # 密码错误
            tkinter.messagebox.showerror(title='Error', message='Password or Username not Correct.')
    else:  # 用户名不存在
        is_sign_up = tkinter.messagebox.askyesno(title='Welcome', message='You have not signed up yet, do you want to sign up?')
        if is_sign_up:  # 调用注册
            user_signup()
        else:
            pass


def user_signup():  # 注册模块
    sign_up_window = tkinter.Toplevel(window)  # 子窗口
    sign_up_window.geometry('350x200')
    sign_up_window.title('Sign up')

    var_new_name = tkinter.StringVar()
    var_new_name.set('example@python.com')  # 预设参数
    var_new_password = tkinter.StringVar()
    var_comfirm_password = tkinter.StringVar()
    
    tkinter.Label(sign_up_window, text='User name:', ).place(x=20, y=30)
    tkinter.Label(sign_up_window, text='Password:', ).place(x=20, y=70)
    tkinter.Label(sign_up_window, text='Comfirm Password:', ).place(x=20, y=110)
    
    new_username_entry = tkinter.Entry(sign_up_window, width=20, textvariable=var_new_name).place(x=150, y=30)
    new_password_entry = tkinter.Entry(sign_up_window, width=20, textvariable=var_new_password, show='*').place(x=150, y=70)
    comfirm_password_entry = tkinter.Entry(sign_up_window, width=20, textvariable=var_comfirm_password, show='*').place(x=150, y=110)


    def comfirm_Signup():  # 确认注册
        with open('user_info.pickle', 'rb') as user_file:
            exist_user_info = pickle.load(user_file)

        new_name = var_new_name.get()
        new_password = var_new_password.get()
        comfirm_password = var_comfirm_password.get()

        str = r'[0-9a-zA-Z]+@[0-9a-zA-Z]+\.com'  # 邮箱的正则表达式模式
        if re.match(str, new_name):  # 合法邮箱
            if new_name in user_info:  # 用户名已存在
                tkinter.messagebox.showerror(title='Error', message='this name has been registered.')
            else:  # 用户名可以注册
                if new_password != comfirm_password:  # 两次密码输入不一致
                    tkinter.messagebox.showerror(title='Error', message='Password inconsistent')
                else:  # 用户名密码正确
                    exist_user_info[new_name] = new_password  # 加入新内容
                    with open('user_info.pickle', 'wb') as user_file:
                        pickle.dump(exist_user_info, user_file)
                    tkinter.messagebox.showinfo(title='Welcome', message='You have successfully signed up')
                    sign_up_window.destroy()
        else:  # 非法邮箱
            tkinter.messagebox.showerror(title='Error', message='Username illegal.')
    

    def cancel_login():  # 取消注册窗口
        sign_up_window.destroy()
    

    Sign_up_btn = tkinter.Button(sign_up_window, text='Comfirm', width=10, command=comfirm_Signup).place(x=70, y=220)
    Cancel_btn = tkinter.Button(sign_up_window, text='Cancel', width=10, command=cancel_login).place(x=200, y=220)

tkinter.Button(window, text='Login', width=10, command=user_login).place(x=220, y=360)  # 主窗口登陆按钮
tkinter.Button(window, text='Sign Up', width=10, command=user_signup).place(x=70, y=360)
window.mainloop()