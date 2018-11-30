import pymysql
db = pymysql.connect("localhost", "root", "kuangjunhao29", "oracle_test")
cursor = db.cursor()


def login():
    s1 = input("1.管理员登陆\t2.学生登陆\n")
    if (s1 == '1'):
        username = input('管理员用户名：')
        pwd = input('管理员密码：')
        if username and pwd:
            sql = 'select * from admin where user = "%s" and passwd = "%s";' % (username, pwd)
            if cursor.execute(sql):
                print('登陆成功')
                admin_select()
            else:
                print('登陆失败, 请重新登录')
                login()
    elif (s1 == '2'):
        username = input('学号：')
        pwd = input('密码：')
        if username and pwd:
            sql = 'select * from student where sno = "%s" and passwd = "%s";' % (username, pwd)
            if cursor.execute(sql):
                print('登陆成功')
                student_select(username)
            else:
                print('登陆失败, 请重新登录')
                login()
    else:
        print('输入无效请重新输入')
        login()

def admin_select():
    print('请选择操作:\n1.添加\t2.删除\t3.修改\t4.统计\t5.退出')
    s = input()
    if(s == '1'):
        sno = input('请输入学生学号:')
        sname = input('请输入学生姓名：')
        spwd = input('请输入初始密码：')
        ssex = input('请输入学生性别：')
        sage = input('请输入学生年龄：')
        sgrade = input('请输入学生学分：')
        sql = 'insert into student values("%s", "%s", "%s", "%s", "%s", "%s");' % (sno, sname, ssex, sgrade, spwd, sage)
        cursor.execute(sql)
        db.commit()
        print('操作完成，返回继续操作')
        admin_select()
    elif(s == '2'):
        sno = input('请输入需要删除的学生学号：')
        sql = 'delete from student where sno="%s";' % sno
        cursor.execute(sql)
        db.commit()
        print('操作完成，返回继续操作')
        admin_select()
    elif(s == '3'):
        sno = input('请输入需要修改的学生学号：')
        sname = input('请输入学生姓名：')
        spwd = input('请输入初始密码：')
        ssex = input('请输入学生性别：')
        sage = input('请输入学生年龄：')
        sgrade = input('请输入学生学分：')
        sql = 'insert into student (sname, ssex, sgrade, sage)values("%s", "%s", "%s", "%s");' % (sname, ssex, sgrade, sage)
        cursor.execute(sql)
        db.commit()
        print('操作完成，返回继续操作')
        admin_select()
    elif(s == '4'):
        print('请选择需要统计的信息：\n1.不同职称老师的数量\t2.不同职称的老师的平均工资\t3.课程平均成绩\n')
        admin_select()
    elif(s == '5'):
        exit()
    else:
        print('输入无效请重新输入')
        admin_select()


def student_select(username):
    s = input('请选择操作:\n1.查看学分\t2.查看选课\t3.修改密码\t4.退出\n')
    if(s == '1'):
        sql = 'select sgrade from student where sno="%s";' % username
        cursor.execute(sql)
        result = cursor.fetchone()
        print('学分：', result[0])
        student_select(username)

    elif(s == '2'):
        sql = 'select * from course'
        cursor.execute(sql)
        results = cursor.fetchall()
        print('课程号    课程名    学分')
        for row in results:
            cno = row[0],
            cname = row[1],
            cgrade = row[2]
            print(row)
        print('操作完成，返回继续操作')
        student_select(username)
    elif(s == '3'):
        new_pwd = input('请输入新密码：')
        sql = 'update student set passwd="%s" where sno="%s";' % (new_pwd, username)
        cursor.execute(sql)
        db.commit()
        print('操作完成，返回继续操作')
        student_select(username)
    elif(s == '4'):
        exit()
    else:
        print('输入无效请重新输入')
        student_select()


login()

cursor.close()
db.close()
