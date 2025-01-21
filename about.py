def func():
    import tkinter, webbrowser

    def websitef(event):
        webbrowser.open_new("www.maniprog.ir")

    def websiteef(event):
        about_window.config(cursor="hand2")

    def websitelf(event):
        about_window.config(cursor="arrow")

    def emailf(event):
        webbrowser.open_new("mailto:info@maniprog.ir")

    def emailef(event):
        about_window.config(cursor="hand2")

    def emaillf(event):
        about_window.config(cursor="arrow")

    def telephonef(event):
        webbrowser.open_new("tel:info@maniprog.ir")

    def telephoneef(event):
        about_window.config(cursor="hand2")

    def telephonelf(event):
        about_window.config(cursor="arrow")
    about_window = tkinter.Tk()
    about_window.geometry("670x300")
    about_window.resizable(0, 0)
    about_window.title("درباره ی نرم افزار")
    about_window.iconbitmap(r"images\window_icon.ico")
    about_window.focus_force()
    software_name = "نرم افزار مدیریت فروشگاه ها مانی"
    tkinter.Label(about_window, font=("B nazanin", 25), text="درباره ی نرم افزار", fg="orangered").pack()
    tkinter.Label(about_window, font=("B nazanin", 15), text="نام نرم افزار: {0}".format(software_name)).place(x=378, y=50)
    tkinter.Label(about_window, font=("B nazanin", 15), text="طراحی، ساخت و برنامه نویسی: موسسه برنامه نویسی مانی").place(x=310, y=90)
    tkinter.Label(about_window, fg="red", font=("B nazanin", 15), text="هرگونه کپی برداری از این نرم افزار بدون داشتن اجازه ی مکتوب از موسسه برنامه نویسی مانی، مجاز نبوده").place(x=10, y=210)
    tkinter.Label(about_window, fg="red", font=("B nazanin", 24, "bold"), text=".و پیگرد قانونی دارد").place(x=230, y=240)
    tkinter.Label(about_window, fg="black", font=("B koodak", 13), text=":شماره تلفن").place(x=580, y=155)
    telephone = tkinter.Label(about_window, fg="blue", font=("B koodak", 13), text="09390185051")
    telephone.bind("<Button-1>", telephonef)
    telephone.bind("<Enter>", telephoneef)
    telephone.bind("<Leave>", telephonelf)
    telephone.place(x=480, y=155)
    tkinter.Label(about_window, fg="black", font=("B koodak", 13), text=":آدرس وبسایت").place(x=370, y=155)
    website = tkinter.Label(about_window, fg="blue", font=("B koodak", 13), text="www.maniprog.ir")
    website.bind("<Button-1>", websitef)
    website.bind("<Enter>", websiteef)
    website.bind("<Leave>", websitelf)
    website.place(x=225, y=155)
    tkinter.Label(about_window, fg="black", font=("B koodak", 13), text=":ایمیل").place(x=160, y=155)
    email = tkinter.Label(about_window, fg="blue", font=("B koodak", 13), text="info@maniprog.ir")
    email.bind("<Button-1>", emailf)
    email.bind("<Enter>", emailef)
    email.bind("<Leave>", emaillf)
    email.place(x=10, y=155)
    about_window.mainloop()
