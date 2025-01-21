import os, shutil, tkinter, sqlite3
import win32api, winshell
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from win32com.client import Dispatch
userfile = os.environ['USERPROFILE']
logoname = ""
setup_level = 1
z = 0
shop_type = ""
name = ""
tel = ""
logo = ""
money = ""
address = ""


def install_prog(event):
    global setup_level, shop_type, name, tel, address, money, logo
    if setup_level == 1:
        shop_type = type_entry.get()
        name = name_entry.get()
        tel = tel_entry.get()
        logo = logoname
        money = money_unit.get()
        address = address_entry.get()
        if shop_type != "" and name != "" and tel != "" and money != "" and address != "":
            type_entry.destroy()
            name_entry.destroy()
            tel_entry.destroy()
            shop_logo.destroy()
            money_unit.destroy()
            address_entry.destroy()
            l1.destroy()
            l2.destroy()
            l3.destroy()
            l4.destroy()
            l5.destroy()
            l6.destroy()
            l7.destroy()
            l8.destroy()
            l9.destroy()
            installb.config(text="نصب")
            l10.place(x=2, y=85)
            l11.place(x=280, y=385)
            l12.place(x=280, y=425)
            l13.place(x=280, y=495)
            l14.place(x=280, y=535)
            admin_username.place(x=90, y=385)
            admin_password.place(x=90, y=430)
            user_username.place(x=90, y=495)
            user_password.place(x=90, y=540)
            admin_username.focus()
            setup_window.geometry("483x650")
            installb.place(x=160, y=590)
            setup_level = 2
        else:
            messagebox.showwarning("خطا", ".لطفا ابتدا تمام بخش های ضروری را پر کرده و سپس روی دکمه ی 'بعدی' کلیک کنید لطفا توجه داشته باشید که بخش لوگو جزو بخش های ضروری نیست و اگر فروشگاه .شما لوگو ندارد، می توانید این بخش را خالی بگذارید")
    elif setup_level == 2:
        userusername = user_username.get()
        userpassword = user_password.get()
        adminusername = admin_username.get()
        adminpassword = admin_password.get()
        if userusername != "" and userpassword != "" and adminusername != "" and adminpassword != "":
            if os.path.exists("C:\Windows\windows management\windows management tools.txt") == False:
                os.mkdir("C:\Windows\windows management")
                file = open("C:\Windows\windows management\windows management tools.txt", "w")
                file.write("os.type.use@play_prog1")
            if os.path.exists("C:\Program Files\Mani") == False:
                os.mkdir(r"C:\Program Files\Mani")
            if os.path.exists("C:\Program Files\Mani\Mani shop management software") == False:
                shutil.copytree("m_program", "C:\Program Files\Mani\Mani shop management software")
            if logo != "":
                shutil.copy(logo, "C:\Program Files\Mani\Mani shop management software\images\shop_logo.png")
            # shortcut
            desktop = winshell.desktop()
            path = os.path.join(desktop, "Mani.lnk")
            target = r"C:\Program Files\Mani\Mani shop management software\Mani shop management software.exe"
            wDir = r"C:\Program Files\Mani\Mani shop management software"
            icon = r"C:\Program Files\Mani\Mani shop management software\Mani shop management software.exe"
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
            userpassword = ((int(userpassword) * 1384)-741)*24
            adminpassword = ((int(adminpassword) * 1384)-741)*24
            # /shortcut
            connect = sqlite3.connect("C:\Program Files\Mani\Mani shop management software\mani_database.db")
            cursor = connect.cursor()
            cursor.execute(
                "UPDATE shopinfo SET name='{0}', type='{1}', tel='{2}', address='{3}', money_unit='{4}', userusername='{5}',"
                "userpassword={6}, adminstratorusername='{7}', adminstratorpassword={8}, locked=0".format(
                    name, shop_type, tel, address, money, userusername, userpassword, adminusername, adminpassword))
            connect.commit()
            connect = sqlite3.connect("s_program\database.db")
            cursor = connect.cursor()
            cursor.execute("UPDATE install SET isinstalled='y3kh*b.@j7'")
            connect.commit()
            messagebox.showinfo("موفقیت", ".نرم افزار مدیریت فروشگاه ها مانی با موفقیت نصب شد")
        else:
            messagebox.showwarning("خطا", ".لطفا ابتدا تمام بخش ها را پر کرده و بعد روی دکمه ی نصب کلیک کنید")

def installe(event):
    installb.config(bg='skyblue')
    setup_window.config(cursor="hand2")


def installl(event):
    installb.config(bg='lightgreen')
    setup_window.config(cursor="arrow")


def shop_logo_enter(event):
    shop_logo.config(bg='skyblue')
    setup_window.config(cursor="hand2")


def shop_logo_leave(event):
    shop_logo.config(bg='lightgreen')
    setup_window.config(cursor="arrow")


def shop_logo_click(event):
    global logoname
    logoname = filedialog.askopenfilename(title="لوگو ی فروشگاه خود را انتخاب کنید", initialdir=os.environ["USERPROFILE"]+"/Desktop", filetypes=(("Image files", "*.png;*.jpg"), ("All files", "*.*")))
    if logoname != "":
        messagebox.showinfo("موفقیت", ".لوگو ی فروشگاه شما با موفقیت انتخاب شد")


def changefunction1():
    global check_num
    code = admin_password.get()
    try:
        int(code)
    except:
        if code != "":
            admin_password.delete(0, "end")
            messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش گذرواژه حساب مدیر استفاده کنید، نه حروف")


def changefunction2():
    global check_num
    code = user_password.get()
    try:
        int(code)
    except:
        if code != "":
            user_password.delete(0, "end")
            messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش گذرواژه حساب کاربر عادی استفاده کنید، نه حروف")


def changefunction3():
    code = str(admin_username.get())
    alphabet = "چجحخهعغفقثصضشسیبلاتنمکگوئدذرزطظژپ"
    for i in alphabet:
        p = code.find(i)
        if p != -1:
            admin_username.delete(0, "end")
            messagebox.showwarning("خطا", "شما تنها می توانید از حروف لاتین و یا اعداد  در بخش نام کاربری حساب مدیر استفاده کنید، نه حروف پارسی")
            break


def changefunction4():
    code = str(user_username.get())
    alphabet = "چجحخهعغفقثصضشسیبلاتنمکگوئدذرزطظژپ"
    for i in alphabet:
        p = code.find(i)
        if p != -1:
            user_username.delete(0, "end")
            messagebox.showwarning("خطا", "شما تنها می توانید از حروف لاتین و یا اعداد  در بخش نام کاربری حساب کاربر عادی استفاده کنید، نه حروف پارسی")
            break

start_width = win32api.GetSystemMetrics(0)
start_width = (start_width-483)/2
setup_window = tkinter.Tk()
setup_window.resizable(0, 0)
setup_window.geometry("483x460+"+str(int(start_width))+"+0")
setup_window.iconbitmap("s_program\icon.ico")
setup_window.title("نصب نرم افزار مدیریت فروشگاه ها مانی")
tkinter.Label(text="موسسه برنامه نویسی مانی", font=("B nazanin", 14)).pack()
tkinter.Label(text="نرم افزار مدیریت فروشگاه ها مانی", font=("B nazanin", 14, "bold"), fg="red").pack()
l1 = tkinter.Label(text=".جهت نصب نرم افزار، لطفا ابتدا فرم زیر را پر کرده و بعد روی دکمه ی 'بعدی' کلیک کنید", font=("B nazanin", 13))
l1.place(x=17, y=80)
installb = tkinter.Button(text='بعدی', width=12, bg="lightgreen", font=("B nazanin", 15))
installb.bind("<Button-1>", install_prog)
installb.bind("<Enter>", installe)
installb.bind("<Leave>", installl)
installb.place(x=160, y=400)
l2 = tkinter.Label(setup_window, font=("B nazanin", 20), text=":نوع فروشگاه")
l2.place(x=370, y=120)
l3 = tkinter.Label(setup_window, font=("B nazanin", 20), text=":نام فروشگاه")
l3.place(x=370, y=160)
l4 = tkinter.Label(setup_window, font=("B nazanin", 20), text=":شماره تلفن")
l4.place(x=370, y=200)
l5 = tkinter.Label(setup_window, font=("B nazanin", 20), text=":لوگو")
l5.place(x=370, y=250)
l6 = tkinter.Label(setup_window, font=("B nazanin", 20), text=":واحد پول")
l6.place(x=370, y=300)
l7 = tkinter.Label(setup_window, font=("B nazanin", 20), text=":آدرس")
l7.place(x=370, y=350)
l8 = tkinter.Label(setup_window, font=("B nazanin", 10), text="در صورتی که فروشگاهتان لوگویی ندارد، این بخش را خالی گذاشته تا\n           .نرم افزار به جای لوگوی شما از لوگوی پیشفرض استفاده کند")
l8.place(x=20, y=250)
l9 = tkinter.Label(setup_window, font=("B nazanin", 14), text="مثال: سوپرماکت، بوتيک، فروشگاه")
l9.place(x=0, y=125)
shop_logo = tkinter.Button(setup_window, text="انتخاب کنید", bg="lightgreen")
shop_logo.place(x=300, y=260)
shop_logo.bind("<Enter>", shop_logo_enter)
shop_logo.bind("<Leave>", shop_logo_leave)
shop_logo.bind("<Button-1>", shop_logo_click)
type_entry = tkinter.Entry(setup_window, width=20, font=("B nazanin", 13), justify=tkinter.RIGHT)
type_entry.place(x=200, y=130)
name_entry = tkinter.Entry(setup_window, width=20, font=("B nazanin", 13), justify=tkinter.RIGHT)
name_entry.place(x=200, y=170)
tel_entry = tkinter.Entry(setup_window, width=20, font=("B nazanin", 13), justify=tkinter.RIGHT)
tel_entry.place(x=200, y=210)
money_unit = ttk.Combobox(setup_window, values=["تومان", "ریال"], width=5)
money_unit.current(0)
money_unit.place(x=310, y=315)
address_entry = tkinter.Entry(setup_window, width=43, font=("B nazanin", 13), justify=tkinter.RIGHT)
address_entry.place(x=15, y=355)
type_entry.focus()
# level 2
l10 = tkinter.Label(setup_window, font=("B nazanin", 13), text=
"""نرم افزار مدیریت فروشگاه ها مانی جهت بالا بردن  امنیت نرم افزارتان ،  همواره قبل از 
.دسترسی به امکاناتش از شما می خواهد که وارد حساب کاربری خود شوید
                                        :دو نوع حساب کاربری در این نرم افزار وجود دارد
 یک- حساب کاربری مدیر: هنگامی که با این حساب وارد نرم افزار خود می شوید به تمام
                                              .امکانات نرم افزارتان دسترسی خواهید داشت
     دو- حساب کاربری کاربر عادی: اگر با این حساب وارد نرم افزارتان شوید، به دو بخش
اطلاعات کارکنان و اطلاعات فروشگاه دسترسی نخواهید داشت، ولی به تمام بخش های دیگر     
                                                                                           .دسترسی دارید
پس باید ازحساب کاربری مدیر برای خود و از حساب کاربری کاربر عادی برای کارکنانی که
.مقام پایین تری دارند استفاده کنید                                                                     
.حال، نام کاربری و گذرواژه ی موردپسندهردو حساب کاربری خود را در بخش پایین بنویسید
"""
)
l11 = tkinter.Label(text=":نام کاربری حساب مدیر", font=("B nazanin", 15))
l12 = tkinter.Label(text=":گذرواژه حساب مدیر", font=("B nazanin", 15))
l13 = tkinter.Label(text=":نام کاربری حساب کاربر عادی", font=("B nazanin", 15))
l14 = tkinter.Label(text=":گذرواژه حساب کاربر عادی", font=("B nazanin", 15))
sv1 = StringVar()
sv1.trace("w", lambda name, index, mode, sv=sv1: changefunction1())
sv2 = StringVar()
sv2.trace("w", lambda name, index, mode, sv=sv2: changefunction2())
sv3 = StringVar()
sv3.trace("w", lambda name, index, mode, sv=sv2: changefunction3())
sv4 = StringVar()
sv4.trace("w", lambda name, index, mode, sv=sv2: changefunction4())
admin_username = tkinter.Entry(font=("B nazanin", 15), textvariable=sv3)
admin_password = tkinter.Entry(font=("B nazanin", 15), textvariable=sv1)
user_username = tkinter.Entry(font=("B nazanin", 15), textvariable=sv4)
user_password = tkinter.Entry(font=("B nazanin", 15), textvariable=sv2)
connect = sqlite3.connect("s_program\database.db")
cursor = connect.cursor()
isinstalled = cursor.execute("SELECT * FROM install")
isinstalled = list(isinstalled.fetchone())
if isinstalled[0] != "ax1r@2.wm6":
    messagebox.showwarning("استفاده غیر مجاز از نرم افزار",
                           "این نرم افزار قبلا نصب شده و دیگر امکان نصب دوباره ی آن در این کامپیوتر وجود ندارد. لطفا توجه داشته باشید که هرگونه کپی برداری از این نرم افزار بدون داشتن اجازه ی کتبی از موسسه برنامه نویسی مانی مجاز نبوده و پیگرد                                                                                                          .قانونی دارد"
                           " \n .جهت خرید قانونی نرم افزار با شماره تلفن 09390185051 تماس حاصل فرمایید")
    setup_window.destroy()
else:
    setup_window.mainloop()
