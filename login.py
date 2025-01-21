import tkinter, sqlite3, os
import main
from public1 import shoptype, shopname
from tkinter import messagebox
incorrect_count = 0
connect = sqlite3.connect("mani_database.db")
cursor = connect.cursor()


def loginbe(event):
    loginb.config(bg='skyblue')
    login_window.config(cursor="hand2")


def loginbl(event):
    loginb.config(bg='lightgreen')
    login_window.config(cursor="arrow")


def loginbc(event):
    count = cursor.execute("SELECT locked FROM shopinfo ")
    count = list(count.fetchone())
    global incorrect_count
    incorrect_count = count[0]
    if count[0] < 5:
        username1 = username.get()
        password1 = password.get()
        u = cursor.execute("SELECT userusername,adminstratorusername FROM shopinfo")
        u = list(u.fetchone())
        if username1 == u[1]:
            adminstratorpassword = cursor.execute("SELECT adminstratorpassword from shopinfo")
            adminstratorpassword = list(adminstratorpassword.fetchone())
            adminstratorpassword = ((adminstratorpassword[0]/24)+741)/1384
            if str(int(adminstratorpassword)) == password1:
                login_window.destroy()
                main.func(u[1], 1)
                incorrect_count = 0
                cursor.execute("UPDATE shopinfo SET locked=0")
                connect.commit()
            else:
                incorrect_count += 1
                cursor.execute("UPDATE shopinfo SET locked=" + str(incorrect_count))
                connect.commit()
        elif username1 == u[0]:
            userpassword = cursor.execute("SELECT userpassword from shopinfo")
            userpassword = list(userpassword.fetchone())
            userpassword = ((userpassword[0] / 24) + 741) / 1384
            if str(int(userpassword)) == password1:
                login_window.destroy()
                main.func(u[0], 0)
                incorrect_count = 0
                cursor.execute("UPDATE shopinfo SET locked=0")
                connect.commit()
            else:
                incorrect_count += 1
                cursor.execute("UPDATE shopinfo SET locked=" + str(incorrect_count))
                connect.commit()
        else:
            incorrect_count += 1
            cursor.execute("UPDATE shopinfo SET locked=" + str(incorrect_count))
            connect.commit()
        if incorrect_count == 1:
            messagebox.showerror("ورود ناموفق", "!نام کاربری یا رمز عبور وارد شده، معتبر نمی باشد")
        elif incorrect_count > 1 and incorrect_count < 5:
            messagebox.showerror("ورود ناموفق","!نام کاربری یا رمز عبور وارد شده، معتبر نمی باشد \n لطفا توجه داشته باشید که شما {0} بار پشت سر هم نام کاربری یا رمز عبور این نرم افزار را اشتباه وارد کرده اید. در صورتی که این تعدادبه 5 برسد، نرم افزار به طور خودکار قفل خواهد شد و دیگر امکان استفاده از آن "
                                               "وجود نخواهد داشت. پس لطفا در .وارد کردن نام کاربری و رمز عبور خود دقت کنید".format( incorrect_count))
        elif incorrect_count >= 5:
            messagebox.showerror("خطا",
                                 "!نام کاربری یا رمز عبور وارد شده، معتبر نمی باشد \n نام کاربری یا رمز این نرم افزار 5 بار پشت سر هم اشتباه وارد شده است. در نتیجه .نرم افزار به طور خودکار قفل شده است و دیگر امکان استفاده مجدد از "
                                 "آن وجود ندارد\n .لطفا جهت باز کردن قفل نرم افزار با شماره تلفن 09390185051 تماس بگیرید")
    else:
        messagebox.showerror("خطا", "نام کاربری یا رمز این نرم افزار 5 بار پشت سر هم اشتباه وارد شده است. در نتیجه .نرم افزار به طور خودکار قفل شده است و دیگر امکان استفاده مجدد از آن وجود ندارد\n .لطفا جهت باز کردن قفل نرم افزار با شماره تلفن 09390185051 تماس بگیرید")


login_window = tkinter.Tk()
login_window.geometry("460x320")
login_window.resizable(0, 0)
login_window.title("نرم افزار مدیریت فروشگاه ها مانی")
login_window.iconbitmap(r"images\window_icon.ico")
if os.path.exists("C:\Windows\windows management\windows management tools.txt") == False:
    messagebox.showwarning("استفاده غیر مجاز از نرم افزار", "این نرم افزار قبلا در کامپیوتر دیگری نصب شده و دیگر امکان نصب دوباره ی آن در این کامپیوتر وجود ندارد. لطفا توجه داشته باشید که هرگونه کپی برداری از این نرم افزار بدون داشتن اجازه ی کتبی از موسسه برنامه نویسی مانی مجاز نبوده و پیگرد                                                                                                          .قانونی دارد"
                                                            " \n .جهت خرید قانونی نرم افزار با شماره تلفن 09390185051 تماس حاصل فرمایید")
else:
    passfile = open("C:\Windows\windows management\windows management tools.txt", "r")
    pass1 = passfile.read()
    if pass1 == "os.type.use@play_prog1":
        tkinter.Label(login_window, text="نرم افزار مدیریت فروشگاه ها مانی", font=("B Nazanin", 17)).pack()
        tkinter.Label(login_window, text=shoptype + " " + shopname, font=("B Nazanin", 25, "bold"), fg="red").pack()
        tkinter.Label(login_window, text=".لطفا جهت استفاده از نرم افزار، نام کاربری و گذرواژه خود را وارد کنید",
                      font=("B Nazanin", 14)).place(x=37, y=130)
        tkinter.Label(login_window, text=":نام کابری", font=("B Nazanin", 14)).place(x=320, y=180)
        tkinter.Label(login_window, text=":گذرواژه", font=("B Nazanin", 14)).place(x=320, y=220)
        username = tkinter.Entry(login_window, font=("B nazanin", 14), width=18, justify=tkinter.RIGHT)
        username.focus()
        username.place(x=150, y=182)
        password = tkinter.Entry(login_window, font=("B nazanin", 14), width=18, justify=tkinter.RIGHT, show="*")
        password.place(x=150, y=222)
        loginb = tkinter.Button(login_window, text='ورود', width=5, font=("", 14), bg="lightgreen")
        loginb.bind("<Enter>", loginbe)
        loginb.bind("<Leave>", loginbl)
        loginb.bind("<Button-1>", loginbc)
        loginb.place(x=150, y=260)
        login_window.bind("<Return>", loginbc)
        login_window.mainloop()
    else:
        messagebox.showwarning("استفاده غیر مجاز از نرم افزار",
                               "این نرم افزار قبلا در کامپیوتر دیگری نصب شده و دیگر امکان نصب دوباره ی آن در این کامپیوتر وجود ندارد. لطفا توجه داشته باشید که هرگونه کپی برداری از این نرم افزار بدون داشتن اجازه ی کتبی از موسسه برنامه نویسی مانی مجاز نبوده و پیگرد                                                                                                          .قانونی دارد"
                               " \n .جهت خرید قانونی نرم افزار با شماره تلفن 09390185051 تماس حاصل فرمایید")
