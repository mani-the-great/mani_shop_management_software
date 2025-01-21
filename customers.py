product_selected = []
check_num = 0


def func():
    import tkinter, sqlite3
    from tkinter import messagebox
    from tkinter import StringVar
    connect = sqlite3.connect("mani_database.db")
    cursor = connect.cursor()

    def newe(event):
        employee_newb.config(bg="skyblue")
        employee_window.config(cursor="hand2")

    def deletee(event):
        employee_deleteb.config(bg="skyblue")
        employee_window.config(cursor="hand2")

    def edite(event):
        employee_editb.config(bg="skyblue")
        employee_window.config(cursor="hand2")

    def submite(event):
        employee_submitb.config(bg="skyblue")
        employee_window.config(cursor="hand2")

    def searche(event):
        employee_searchb.config(bg="skyblue")
        employee_window.config(cursor="hand2")

    def exite(event):
        employee_exitb.config(bg="skyblue")
        employee_window.config(cursor="hand2")

    def newl(event):
        employee_newb.config(bg="lightgreen")
        employee_window.config(cursor="arrow")

    def deletel(event):
        employee_deleteb.config(bg="lightgreen")
        employee_window.config(cursor="arrow")

    def editl(event):
        employee_editb.config(bg="lightgreen")
        employee_window.config(cursor="arrow")

    def submitl(event):
        employee_submitb.config(bg="lightgreen")
        employee_window.config(cursor="arrow")

    def searchl(event):
        employee_searchb.config(bg="lightgreen")
        employee_window.config(cursor="arrow")

    def exitl(event):
        employee_exitb.config(bg="red")
        employee_window.config(cursor="arrow")
    # do

    def exitc(event):
        employee_window.destroy()

    def newc(event):
        if employee_newb.cget("state") == "normal":
            product_code.config(state="normal")
            result = cursor.execute("SELECT max(code) FROM customer")
            row = list(result.fetchone())
            if row[0] == None:
                row[0] = 0
            product_code.delete(0, "end")
            product_name.delete(0, "end")
            product_amount.delete(0, "end")
            product_details.delete("1.0", "end")
            product_unit.delete(0, "end")
            product_code.insert(0, str(row[0]+1))
            employee_newb.config(state="normal")
            employee_deleteb.config(state="disabled")
            employee_editb.config(state="disabled")
            employee_submitb.config(state="normal")
            product_code.config(state="normal")
            product_code.focus()
    def deletec(event):
        if employee_deleteb.cget("state") == "normal":
            code = product_code.get()
            if code != "":
                try:
                    cursor.execute("DELETE FROM customer WHERE code=" + code)
                    connect.commit()
                except:
                    messagebox.showerror("خطا", "!اطلاعات این کارکن حذف نشدند")
                else:
                    messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت حذف شدند")

    def editc(event):
        if employee_editb.cget("state") == "normal":
            code = product_code.get()
            name = product_name.get()
            tel = product_amount.get()
            address = product_unit.get()
            details = product_details.get("1.0", "end")
            if code != "":
                try:
                    cursor.execute("UPDATE customer SET name='{0}', tel='{1}', address='{2}',"
                                   "details='{3}'  WHERE code={4}".format(
                        name, tel, address, details, int(code)))
                    connect.commit()
                except:
                    messagebox.showerror("خطا", "!اطلاعات این کارکن ویرایش نشدند")
                else:
                    messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت ویرایش شدند")

    def submitc(event):
        if employee_submitb.cget("state") == "normal":
            code = product_code.get()
            name = product_name.get()
            tel = product_amount.get()
            address = product_unit.get()
            details = product_details.get("1.0", "end")
            if name != "" and code != "":
                cursor.execute("INSERT INTO customer(name,code,tel,address,details)"
                               "VALUES('{0}','{1}','{2}','{3}','{4}')".format(
                                name, code, tel, address, details))
                connect.commit()
                messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت ثبت شدند")
                employee_newb.config(state="normal")
                product_code.config(state="readonly")
                employee_submitb.config(state="disabled")
            else:
                messagebox.showerror("اخطار", ".لطفا ابتدا تمام بخش های ضروری(ستاره دار) را پر کرده و بعد اقدام به ثبت آن کنید")
# as

    def searchc(event):
        # start
        from tkinter import ttk

        # as

        def select_employee(event):
            selected = list(tree.item(tree.focus())['values'])
            global product_selected
            product_selected = selected
            product_code.config(state="normal")
            product_code.delete(0, "end")
            product_name.delete(0, "end")
            product_amount.delete(0, "end")
            product_unit.delete(0, "end")
            product_details.delete("1.0", "end")
            product_selected.reverse()
            product_code.insert(0, product_selected[0])
            product_name.insert(0, product_selected[1])
            product_amount.insert(0, product_selected[2])
            product_unit.insert(0, str(product_selected[3]))
            product_details.insert("0.5", product_selected[4])
            employee_deleteb.config(state="normal")
            employee_editb.config(state="normal")
            product_code.config(state="readonly")
            employee_search_window.destroy()

        employee_search_window = tkinter.Tk()
        employee_search_window.resizable(0, 0)
        employee_search_window.title("جستجو ی مشتریان")
        employee_search_window.iconbitmap(r"images\window_icon.ico")
        employee_search_window.focus_force()
        tkinter.Label(employee_search_window,
                      text="کلیک کنید" + " Enter " + "جهت انتخاب یکی از مشتریان، بعد از انتخاب آن، روی دکمه ی ",
                      font=("B nazanin", 13)).pack()
        tree = ttk.Treeview(employee_search_window, height=15)
        tree.pack()
        tree["columns"] = ("1", "2", "3", "4", "5")
        tree['show'] = 'headings'
        tree.column("1", width=150, anchor='c')
        tree.column("2", width=150, anchor='c')
        tree.column("3", width=90, anchor='c')
        tree.column("4", width=150, anchor='c')
        tree.column("5", width=90, anchor='c')
        tree.heading("1", text="توضیحات")
        tree.heading("2", text="آدرس")
        tree.heading("3", text="شماره تلفن")
        tree.heading("4", text="نام")
        tree.heading("5", text="کد")
        # values
        e = cursor.execute("SELECT * FROM customer")
        productlist = list(e.fetchall())
        for i in productlist:
            product = list(i)
            product.reverse()
            tree.insert("", "end", values=(product))
        employee_search_window.bind("<Return>", select_employee)
        employee_search_window.mainloop()
        # end

    def changefunction1():
        global check_num
        if check_num == 1:
            code = product_code.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    product_code.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش کد مشتری استفاده کنید، نه حروف")

    employee_window = tkinter.Tk()
    employee_window.geometry("500x440")
    employee_window.resizable(0, 0)
    employee_window.title("مشتریان")
    employee_window.focus_force()
    employee_window.iconbitmap(r"images\window_icon.ico")
    # labels
    tkinter.Label(employee_window, font=("B nazanin", 25), fg="orangered", text="مشتریان").pack()
    tkinter.Label(employee_window, font=("", 17), text=":(*)کد مشتری").place(x=360, y=50)
    tkinter.Label(employee_window, font=("", 17), text=":(*)نام مشتری").place(x=360, y=100)
    tkinter.Label(employee_window, font=("", 17), text=":شماره تلفن").place(x=360, y=150)
    tkinter.Label(employee_window, font=("", 17), text=":آدرس").place(x=360, y=200)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":توضیحات").place(x=360, y=250)
    # /labels
    # Entries and texts
    sv1 = StringVar()
    sv1.trace("w", lambda name, index, mode, sv=sv1: changefunction1())
    product_code = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT, state="readonly", textvariable=sv1)
    product_code.place(x=170, y=55)
    product_name = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    product_name.place(x=170, y=105)
    product_amount = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    product_amount.place(x=170, y=155)
    product_unit = tkinter.Entry(employee_window, width=43, font=("B nazanin", 13), justify=tkinter.RIGHT)
    product_unit.place(x=10, y=205)
    product_details = tkinter.Text(employee_window, font=("B nazanin", 13), height=3, width=43)
    product_details.place(x=10, y=255)
    global check_num
    check_num = 1
    # /Entries and texts
    # Buttons
    employee_newb = tkinter.Button(employee_window, text="جدید", font=("B nazanin", 16), bg="lightgreen")
    employee_newb.bind("<Enter>", newe)
    employee_newb.bind("<Leave>", newl)
    employee_newb.bind("<Button-1>", newc)
    employee_newb.place(x=430, y=350)
    employee_deleteb = tkinter.Button(employee_window, state="disabled", text="حذف", font=("B nazanin", 16), bg="lightgreen")
    employee_deleteb.bind("<Enter>", deletee)
    employee_deleteb.bind("<Leave>", deletel)
    employee_deleteb.bind("<Button-1>", deletec)
    employee_deleteb.place(x=360, y=350)
    employee_editb = tkinter.Button(employee_window, state="disabled", text="ویرایش", font=("B nazanin", 16), bg="lightgreen")
    employee_editb.bind("<Enter>", edite)
    employee_editb.bind("<Leave>", editl)
    employee_editb.bind("<Button-1>", editc)
    employee_editb.place(x=275, y=350)
    employee_submitb = tkinter.Button(employee_window, state="disabled", text="ثبت اطلاعات", font=("B nazanin", 16), bg="lightgreen")
    employee_submitb.bind("<Enter>", submite)
    employee_submitb.bind("<Leave>", submitl)
    employee_submitb.bind("<Button-1>", submitc)
    employee_submitb.place(x=160, y=350)
    employee_searchb = tkinter.Button(employee_window, text="جستجو", font=("B nazanin", 16), bg="lightgreen")
    employee_searchb.bind("<Enter>", searche)
    employee_searchb.bind("<Leave>", searchl)
    employee_searchb.bind("<Button-1>", searchc)
    employee_searchb.place(x=80, y=350)
    employee_exitb = tkinter.Button(employee_window, text="خروج", font=("B nazanin", 16), bg="red")
    employee_exitb.bind("<Enter>", exite)
    employee_exitb.bind("<Leave>", exitl)
    employee_exitb.bind("<Button-1>", exitc)
    employee_exitb.place(x=10, y=370)
    # /Buttons
    employee_window.mainloop()
#func()