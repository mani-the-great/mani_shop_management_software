def func():
    import reminder
    import tkinter, os
    from tkinter import messagebox

    def calculatorbe(event):
        calculatorb.config(bg='skyblue')
        etc_window.config(cursor="hand2")

    def calculatorbl(event):
        calculatorb.config(bg='lightgreen')
        etc_window.config(cursor="arrow")

    def calculatorbc(event):
        if os.path.exists("C:\Windows\system32\calc.exe"):
            os.startfile("C:\Windows\system32\calc.exe")
        else:
            messagebox.showerror("خطا", "!نرم افزار ماشین حساب حذف شده است و دیگر در رایانه شما وجود ندارد")

    def reminderbe(event):
        reminderb.config(bg='skyblue')
        etc_window.config(cursor="hand2")

    def reminderbl(event):
        reminderb.config(bg='lightgreen')
        etc_window.config(cursor="arrow")

    def reminderbc(event):
        reminder.func()

    etc_window = tkinter.Tk()
    etc_window.geometry("300x300")
    etc_window.resizable(0, 0)
    etc_window.title("سایر امکانات")
    etc_window.iconbitmap(r"images\window_icon.ico")
    etc_window.focus_force()
    tkinter.Label(etc_window, text="سایر امکانات نرم افزار", font=("B Nazanin", 20), fg="orangered").pack()
    calculatorb = tkinter.Button(etc_window, text='ماشین حساب', width=15, font=("", 18), bg="lightgreen")
    calculatorb.bind("<Enter>", calculatorbe)
    calculatorb.bind("<Leave>", calculatorbl)
    calculatorb.bind("<Button-1>", calculatorbc)
    calculatorb.place(x=40, y=50)
    reminderb = tkinter.Button(etc_window, text='یادداشت ها', width=15, font=("", 18), bg="lightgreen")
    reminderb.bind("<Enter>",  reminderbe)
    reminderb.bind("<Leave>",  reminderbl)
    reminderb.bind("<Button-1>",  reminderbc)
    reminderb.place(x=40, y=110)
    etc_window.mainloop()
#func()