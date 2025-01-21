from public1 import *
from datetime import *
from tkinter import *
from PIL import ImageTk, Image
do_timer = 1


def func(user, type):
    from tkinter import messagebox
    import sys
    import win32api
    win32api.LoadKeyboardLayout('00000429', 1)
    try:
        import tkinter, threading, functools
        import shamsidate, about, shop_info, employee_info, products, customers, etc, sell, report

        def aboutbc(event):
            about.func()

        def shopbc(event):
            if type == 1:
                shop_info.func()
            else:
                messagebox.showerror("خطا", "شما با حساب کاربری 'کاربر عادی' وارد نرم افزار شده اید. بنابراین اجازه ی دسترسی به بخش 'اطلاعات فروشگاه' را ندارید. در صورتی که می خواهید به این بخش دسترسی داشته باشید باید با حساب کاربری مدیر وارد"
                                            )

        def productbe(event):
            productb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def productbl(event):
            productb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def productbc(event):
            products.func()

        def sellbe(event):
            sellb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def sellbl(event):
            sellb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def sellbc(event):
            sell.func()

        def reportbe(event):
            reportb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def reportbl(event):
            reportb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def reportbc(event):
            report.func()

        def aboutbe(event):
            aboutb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def aboutbl(event):
            aboutb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def shopbe(event):
            shopb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def shopbl(event):
            shopb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def employeebe(event):
            employeeb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def employeebl(event):
            employeeb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def employeebc(event):
            if type == 1:
                employee_info.func()
            else:
                messagebox.showerror("خطا", "شما با حساب کاربری 'کاربر عادی' وارد نرم افزار شده اید. بنابراین اجازه ی دسترسی به بخش 'اطلاعات کارکنان' را ندارید. در صورتی که می خواهید به این بخش دسترسی داشته باشید باید با حساب کاربری مدیر وارد"
                                     " نرم افزار شوید. زیرا فقط حساب کاربری مدیر اجازه ی دسترسی به این بخش را دارد")

        def etcbe(event):
            etcb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def etcbl(event):
            etcb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def etcc(event):
            etc.func()

        def customerbe(event):
            customerb.config(bg='skyblue')
            main_window.config(cursor="hand2")

        def customerbl(event):
            customerb.config(bg='lightgreen')
            main_window.config(cursor="arrow")

        def customerbc(event):
            customers.func()

        def exit_program():

            def exitbe(event):
                exitb.config(bg='skyblue')
                exit_window.config(cursor="hand2")

            def exitbl(event):
                exitb.config(bg='red')
                exit_window.config(cursor="arrow")

            def exitbc(event):
                exit_window.destroy()
                main_window.destroy()

            def notexitbe(event):
                notexitb.config(bg='skyblue')
                exit_window.config(cursor="hand2")

            def notexitbl(event):
                notexitb.config(bg='lightgreen')
                exit_window.config(cursor="arrow")

            def notexitbc(event):
                exit_window.destroy()

            global do_timer
            do_timer = 0
            exit_window = tkinter.Tk()
            exit_window.geometry("370x110")
            exit_window.resizable(0, 0)
            exit_window.title("خروج از نرم افزار")
            exit_window.iconbitmap(r"images\window_icon.ico")
            exit_window.focus_force()
            tkinter.Label(exit_window, font=("B nazanin", 15),
                          text="آیا مطمئن هستید که می خواهید از نرم افزار خارج شوید؟").pack()
            exitb = tkinter.Button(exit_window, text='بله', width=6, font=("", 18), bg="red")
            exitb.bind("<Enter>", exitbe)
            exitb.bind("<Leave>", exitbl)
            exitb.bind("<Button-1>", exitbc)
            exitb.place(x=190, y=50)
            notexitb = tkinter.Button(exit_window, text='خیر', width=6, font=("", 18), bg="lightgreen")
            notexitb.bind("<Enter>", notexitbe)
            notexitb.bind("<Leave>", notexitbl)
            notexitb.bind("<Button-1>", notexitbc)
            notexitb.place(x=70, y=50)
            exit_window.mainloop()

        main_window = tkinter.Tk()
        start_width = win32api.GetSystemMetrics(0)
        start_height = win32api.GetSystemMetrics(1)
        start_width = (start_width-800)/2
        start_height = (start_height - 600) / 2
        main_window.geometry("800x600+"+str(int(start_width))+"+"+ str(int(start_height)))
        main_window.resizable(0, 0)
        main_window.title("نرم افزار مدیریت فروشگاه ها مانی")
        main_window.iconbitmap(r"images\window_icon.ico")
        main_window.focus_force()
        tkinter.Label(text="نرم افزار مدیریت فروشگاه ها مانی", font=("B Nazanin", 17)).pack()
        tkinter.Label(text=shoptype + " " + shopname, font=("B Nazanin", 33, "bold"), fg="red").pack()
        # buttons
        productb = tkinter.Button(text='کالا', width=15, font=("", 18), bg="lightgreen")
        productb.bind("<Enter>", productbe)
        productb.bind("<Leave>", productbl)
        productb.bind("<Button-1>", productbc)
        productb.place(x=550, y=150)
        sellb = tkinter.Button(text='فروش', width=15, font=("", 18), bg="lightgreen")
        sellb.bind("<Enter>", sellbe)
        sellb.bind("<Leave>", sellbl)
        sellb.bind("<Button-1>", sellbc)
        sellb.place(x=550, y=225)
        reportb = tkinter.Button(text='گزارشات', width=15, font=("", 18), bg="lightgreen")
        reportb.bind("<Enter>", reportbe)
        reportb.bind("<Leave>", reportbl)
        reportb.bind("<Button-1>", reportbc)
        reportb.place(x=550, y=300)
        customerb = tkinter.Button(text='مشتریان', width=15, font=("", 18), bg="lightgreen")
        customerb.bind("<Enter>", customerbe)
        customerb.bind("<Leave>", customerbl)
        customerb.bind("<Button-1>", customerbc)
        customerb.place(x=550, y=375)
        employeeb = tkinter.Button(text='اطلاعات کارکنان', width=15, font=("", 18), bg="lightgreen")
        employeeb.bind("<Enter>", employeebe)
        employeeb.bind("<Leave>", employeebl)
        employeeb.bind("<Button-1>", employeebc)
        employeeb.place(x=30, y=150)
        shopb = tkinter.Button(text='اطلاعات ' + shoptype, width=15, font=("", 18), bg="lightgreen")
        shopb.bind("<Enter>", shopbe)
        shopb.bind("<Leave>", shopbl)
        shopb.bind("<Button-1>", shopbc)
        shopb.place(x=30, y=225)
        aboutb = tkinter.Button(text='درباره ی نرم افزار', width=15, font=("", 18), bg="lightgreen")
        aboutb.bind("<Enter>", aboutbe)
        aboutb.bind("<Leave>", aboutbl)
        aboutb.bind("<Button-1>", aboutbc)
        aboutb.place(x=30, y=300)
        etcb = tkinter.Button(text='سایر امکانات', width=15, font=("", 18), bg="lightgreen")
        etcb.bind("<Enter>", etcbe)
        etcb.bind("<Leave>", etcbl)
        etcb.bind("<Button-1>", etcc)
        etcb.place(x=30, y=375)
        # \buttons
        tkinter.Label(font=("B nazanin", 20), text=":ساعت ").place(x=700, y=450)
        clock = tkinter.Label(fg='#8B3A10', font=("B nazanin", 20), text=datetime.now().strftime("%H:%M:%S"))
        tkinter.Label(fg='#8B3A10', font=("B nazanin", 20), text=shamsidate.sdate).place(x=400, y=450)
        tkinter.Label(font=("B nazanin", 20), text=":تاریخ ").place(x=510, y=450)
        tkinter.Label(fg='#8B3A10', font=("B nazanin", 20), text='09390185051').place(x=10, y=450)
        tkinter.Label(font=("B nazanin", 20), text=":شماره تلفن پشتیبانی ").place(x=160, y=450)
        tkinter.Label(font=("B nazanin", 15),
                      text=""".تمامی حقوق مادی و معنوی این نرم افزار برای موسسه برنامه نویسی مانی محفوظ است -""").place(x = 42, y=530)
        welcome_lable = tkinter.Label(font=("B nazanin", 14), text=".به حساب کاربری خود خوش آمدید {0}".format(user), fg="green")
        if len(user) <= 7:
            welcome_lable.place(x=500, y=103)
        elif len(user) <= 12:
            welcome_lable.place(x=440, y=103)
        elif len(user) <= 17:
            welcome_lable.place(x=370, y=103)
        elif len(user) <= 22:
            welcome_lable.place(x=290, y=103)
        else:
            welcome_lable.place(x=200, y=103)
        copyright1 = tkinter.Label(font=("B nazanin", 15, "bold"), text="موسسه برنامه نویسی مانی")
        copyright1.place(x=586, y=528)
        tkinter.Label(font=("B nazanin", 15), text="©").place(x=771, y=533)
        # logo image
        img_location = "images/shop_logo.png"
        img = Image.open(img_location)
        img = img.resize((285, 265), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(main_window, image=img)
        panel.image = img
        # / logo image
        panel.place(x=255, y=190)
        clock.place(x=600, y=450)

        def time_timer():
            if do_timer == 1:
                threading.Timer(1, time_timer).start()
                clock.config(text=datetime.now().strftime("%H:%M:%S"))

        time_timer()

        def mani_timer():
            if do_timer == 1:
                threading.Timer(2, mani_timer).start()
                if copyright1.cget("fg") == "black":
                    copyright1.config(fg="red")
                else:
                    copyright1.config(fg="black")

        mani_timer()
        main_window.protocol("WM_DELETE_WINDOW", exit_program)
        main_window.mainloop()
    except:
        messagebox.showerror("خطا",
                             "در هنگام اجرای برنامه خطایی رخ داد. لطفا جهت رفع این خطا با شماره تلفن .پشتیبانی تماس بگیرید  \n شماره تلفن پشتیبانی: 09390185051   \n{0} :نام ارور".format(
                                 str(sys.exc_info()[0])))


#func("admin", 1)
