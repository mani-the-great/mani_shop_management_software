logoname = ""


def func():
    import tkinter, shutil, sqlite3, os
    from public1 import shoptype, shopname, shoptel, shopaddress, shop_money_unit
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import messagebox

    def shop_exit_enter(event):
        shop_exit.config(bg='skyblue')
        shop_window.config(cursor="hand2")

    def shop_exit_leave(event):
        shop_exit.config(bg='red')
        shop_window.config(cursor="arrow")

    def shop_exit_click(event):
        shop_window.destroy()

    def shop_edit_enter(event):
        shop_edit.config(bg='skyblue')
        shop_window.config(cursor="hand2")

    def shop_edit_leave(event):
        shop_edit.config(bg='lightgreen')
        shop_window.config(cursor="arrow")

    def shop_edit_click(event):
        connect = sqlite3.connect("mani_database.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE shopinfo SET name='{0}', address='{1}', tel={2}, money_unit='{3}'".format(name_entry.get(), address_entry.get(), tel_entry.get(), money_unit.get()))
        connect.commit()
        if logoname != "":
            shutil.copy(logoname, r"images\shop_logo.png")
        messagebox.showinfo("موفقیت", ".اطلاعات "+shoptype+" شما با موفقیت ویرایش شدند")

    def shop_logo_enter(event):
        shop_logo.config(bg='skyblue')
        shop_window.config(cursor="hand2")

    def shop_logo_leave(event):
        shop_logo.config(bg='lightgreen')
        shop_window.config(cursor="arrow")

    def shop_logo_click(event):
        global logoname
        logoname = filedialog.askopenfilename(title="لوگو ی "+shoptype+" خود را انتخاب کنید", initialdir=os.environ["USERPROFILE"]+"/Desktop", filetypes=(("Image files", "*.png;*.jpg"), ("All files", "*.*")))
        if logoname != "":
            messagebox.showinfo("موفقیت", "لوگو ی "+shoptype+" شما با موفقیت انتخاب شد. جهت ذخیره ی این لوگو، روی دکمه ی .ویرایش' کلیک کنید'")

    shop_window = tkinter.Tk()
    shop_window.geometry("500x400")
    shop_window.resizable(0, 0)
    shop_window.title("اطلاعات " + shoptype)
    shop_window.iconbitmap(r"images\window_icon.ico")
    shop_window.focus_force()
    tkinter.Label(shop_window, font=("B nazanin", 25), fg="orangered", text="اطلاعات "+shoptype+" "+shopname).pack()
    tkinter.Label(shop_window, font=("B nazanin", 20), text=":نام "+shoptype).place(x=380, y=50)
    tkinter.Label(shop_window, font=("B nazanin", 20), text=":شماره تلفن").place(x=380, y=100)
    tkinter.Label(shop_window, font=("B nazanin", 20), text=":لوگو").place(x=380, y=150)
    tkinter.Label(shop_window, font=("B nazanin", 20), text=":واحد پول").place(x=380, y=200)
    tkinter.Label(shop_window, font=("B nazanin", 20), text=":آدرس").place(x=380, y=250)
    shop_logo = tkinter.Button(shop_window, text="انتخاب کنید", bg="lightgreen")
    shop_logo.place(x=310, y=160)
    shop_logo.bind("<Enter>", shop_logo_enter)
    shop_logo.bind("<Leave>", shop_logo_leave)
    shop_logo.bind("<Button-1>", shop_logo_click)
    shop_edit = tkinter.Button(shop_window, text="ویرایش", width=6, font=("B nazanin", 16), bg="lightgreen")
    shop_edit.place(x=120, y=320)
    shop_edit.bind("<Enter>", shop_edit_enter)
    shop_edit.bind("<Leave>", shop_edit_leave)
    shop_edit.bind("<Button-1>", shop_edit_click)
    shop_exit = tkinter.Button(shop_window, text="خروج", width=6, font=("B nazanin", 16), bg="red")
    shop_exit.place(x=20, y=320)
    shop_exit.bind("<Enter>", shop_exit_enter)
    shop_exit.bind("<Leave>", shop_exit_leave)
    shop_exit.bind("<Button-1>", shop_exit_click)
    name_entry = tkinter.Entry(shop_window, width=20, font=("B nazanin", 13), justify=tkinter.RIGHT)
    name_entry.place(x=210, y=60)
    tel_entry = tkinter.Entry(shop_window, width=20, font=("B nazanin", 13), justify=tkinter.RIGHT)
    tel_entry.place(x=210, y=110)
    money_unit = ttk.Combobox(shop_window, values=["تومان", "ریال"], width=5)
    money_unit.place(x=320, y=215)
    address_entry = tkinter.Entry(shop_window, width=43, font=("B nazanin", 13), justify=tkinter.RIGHT)
    address_entry.place(x=25, y=260)
    tel_entry.insert(0, shoptel)
    name_entry.insert(0, shopname)
    address_entry.insert(0, shopaddress)
    if shop_money_unit == "ریال":
        money_unit.current(1)
    else:
        money_unit.current(0)
    shop_window.mainloop()
