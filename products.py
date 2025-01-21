product_selected = []
check_num = 0

def func():
    import tkinter, sqlite3
    from tkinter import messagebox
    from public1 import shop_money_unit
    from tkinter import ttk
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
            global check_num
            check_num = 0
            product_code.config(state="normal")
            result = cursor.execute("SELECT max(code) FROM product")
            row = list(result.fetchone())
            if row[0] == None:
                row[0] = 0
            product_code.delete(0, "end")
            product_name.delete(0, "end")
            product_amount.delete(0, "end")
            product_details.delete("1.0", "end")
            product_unit.delete(0, "end")
            product_seller.delete(0, "end")
            product_buyprice.delete(0, "end")
            product_sellprice.delete(0, "end")
            product_ispaid.delete(0, "end")
            product_code.insert(0, str(row[0]+1))
            employee_newb.config(state="normal")
            employee_deleteb.config(state="disabled")
            employee_editb.config(state="disabled")
            employee_submitb.config(state="normal")
            product_code.config(state="normal")
            product_ispaid.current(0)
            product_code.focus()
            check_num = 1

    def deletec(event):
        if employee_deleteb.cget("state") == "normal":
            code = product_code.get()
            if code != "":
                try:
                    cursor.execute("DELETE FROM product WHERE code=" + code)
                    connect.commit()
                except:
                    messagebox.showerror("خطا", "!اطلاعات این کارکن حذف نشدند")
                else:
                    messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت حذف شدند")

    def editc(event):
        if employee_editb.cget("state") == "normal":
            code = product_code.get()
            name = product_name.get()
            amount = product_amount.get()
            unit = product_unit.get()
            details = product_details.get("1.0", "end")
            seller = product_seller.get()
            buyprice = product_buyprice.get()
            ispaid = product_ispaid.get()
            sellprice = product_sellprice.get()
            if code != "":
                try:
                    cursor.execute("UPDATE product SET name='{0}', amount='{1}', unit='{2}',"
                                   "details='{3}', seller='{4}', buyprice='{5}', sellprice='{6}',  ispaid='{7}'  WHERE code={8}".format(
                        name, amount, unit, details, seller, buyprice, sellprice, ispaid, int(code)))
                    connect.commit()
                except:
                    messagebox.showerror("خطا", "!اطلاعات این کارکن ویرایش نشدند")
                else:
                    messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت ویرایش شدند")

    def submitc(event):
        if employee_submitb.cget("state") == "normal":
            code = product_code.get()
            name = product_name.get()
            amount = product_amount.get()
            unit = product_unit.get()
            details = product_details.get("1.0", "end")
            seller = product_seller.get()
            buyprice = product_buyprice.get()
            ispaid = product_ispaid.get()
            sellprice = product_sellprice.get()
            if name != "" and amount != "" and unit != "" and code != "" and sellprice != "":
                cursor.execute("INSERT INTO product(name,amount,unit,details,seller,buyprice,sellprice,ispaid,code)"
                               "VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}', {8})".format(
                                name, amount, unit, details, seller, buyprice, sellprice, ispaid, code))
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
            product_seller.delete(0, "end")
            product_buyprice.delete(0, "end")
            product_sellprice.delete(0, "end")
            product_ispaid.delete(0, "end")
            product_selected.reverse()
            product_code.insert(0, product_selected[0])
            product_name.insert(0, product_selected[1])
            product_amount.insert(0, product_selected[2])
            product_unit.insert(0, str(product_selected[3]))
            product_seller.insert(0, product_selected[4])
            product_buyprice.insert(0, product_selected[5])
            product_sellprice.insert(0, product_selected[6])
            product_ispaid.insert(0, product_selected[7])
            product_details.insert("0.5", product_selected[8])
            employee_deleteb.config(state="normal")
            employee_editb.config(state="normal")
            product_code.config(state="readonly")
            employee_search_window.destroy()

        employee_search_window = tkinter.Tk()
        employee_search_window.resizable(0, 0)
        employee_search_window.title("جستجو ی کالا")
        employee_search_window.iconbitmap(r"images\window_icon.ico")
        tkinter.Label(employee_search_window,
                      text="کلیک کنید" + " Enter " + "جهت انتخاب یکی از کالا ها، بعد از انتخاب آن، روی دکمه ی ",
                      font=("B nazanin", 13)).pack()
        tree = ttk.Treeview(employee_search_window, height=20)
        tree.pack()
        tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        tree['show'] = 'headings'
        tree.column("1", width=150, anchor='c')
        tree.column("2", width=90, anchor='c')
        tree.column("3", width=90, anchor='c')
        tree.column("4", width=90, anchor='c')
        tree.column("5", width=150, anchor='c')
        tree.column("6", width=90, anchor='c')
        tree.column("7", width=90, anchor='c')
        tree.column("8", width=90, anchor='c')
        tree.column("9", width=90, anchor='c')
        tree.heading("1", text="توضیحات")
        tree.heading("2", text="پرداخت هزینه")
        tree.heading("3", text="قیمت فروش")
        tree.heading("4", text="قیمت خرید")
        tree.heading("5", text="فروشنده")
        tree.heading("6", text="واحد")
        tree.heading("7", text="تعداد/مقدار")
        tree.heading("8", text="نام")
        tree.heading("9", text="کد")
        # values
        e = cursor.execute("SELECT * FROM product")
        productlist = list(e.fetchall())
        for i in productlist:
            product = list(i)
            product.reverse()
            tree.insert("", "end", values=(product))
        employee_search_window.bind("<Return>", select_employee)
        employee_search_window.focus_force()
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
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش کد کالا استفاده کنید، نه حروف")

    def changefunction2():
        global check_num
        if check_num == 1:
            code = product_amount.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    product_amount.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش تعداد کالا استفاده کنید، نه حروف")
    def changefunction3():
        global check_num
        if check_num == 1:
            code = product_sellprice.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    product_sellprice.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش قیمت فروش استفاده کنید، نه حروف")

    employee_window = tkinter.Tk()
    employee_window.geometry("500x640")
    employee_window.resizable(0, 0)
    employee_window.title("کالا")
    employee_window.focus_force()
    employee_window.iconbitmap(r"images\window_icon.ico")
    # labels
    tkinter.Label(employee_window, font=("B nazanin", 25), fg="orangered", text="کالا").pack()
    tkinter.Label(employee_window, font=("", 17), text=":(*)کد کالا").place(x=360, y=50)
    tkinter.Label(employee_window, font=("", 17), text=":(*)نام کالا").place(x=360, y=100)
    tkinter.Label(employee_window, font=("", 17), text=":(*)تعداد/مقدار").place(x=360, y=150)
    tkinter.Label(employee_window, font=("", 17), text=":(*)واحد").place(x=360, y=200)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":فروشنده ی کالا").place(x=360, y=250)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":قیمت خرید").place(x=360, y=300)
    tkinter.Label(employee_window, font=("", 17), text=":(*)قیمت فروش").place(x=360, y=350)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":پرداخت هزینه").place(x=360, y=400)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":توضیحات").place(x=360, y=450)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=shop_money_unit).place(x=115, y=300)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=shop_money_unit).place(x=115, y=350)
    # /labels
    # Entries and texts
    sv1 = StringVar()
    sv1.trace("w", lambda name, index, mode, sv=sv1: changefunction1())
    sv2 = StringVar()
    sv2.trace("w", lambda name, index, mode, sv=sv2: changefunction2())
    sv3 = StringVar()
    sv3.trace("w", lambda name, index, mode, sv=sv3: changefunction3())
    product_code = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT, state="readonly", textvariable=sv1)
    product_code.place(x=170, y=55)
    product_name = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    product_name.place(x=170, y=105)
    product_amount = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT, textvariable=sv2)
    product_amount.place(x=170, y=155)
    product_unit = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    product_unit.place(x=170, y=205)
    product_seller = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    product_seller.place(x=170, y=255)
    product_buyprice = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    product_buyprice.place(x=170, y=305)
    product_sellprice = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT, textvariable=sv3)
    product_sellprice.place(x=170, y=355)
    product_ispaid = ttk.Combobox(employee_window, values=["هزینه ی این کالا پرداخت شده است", "هزینه ی این کالا هنوز پرداخت نشده است"], font=("B nazanin", 13), width=27)
    product_ispaid.current(0)
    product_ispaid.place(x=120, y=405)
    product_details = tkinter.Text(employee_window, font=("B nazanin", 13), height=3, width=43)
    product_details.place(x=10, y=455)
    # /Entries and texts
    # Buttons
    employee_newb = tkinter.Button(employee_window, text="جدید", font=("B nazanin", 16), bg="lightgreen")
    employee_newb.bind("<Enter>", newe)
    employee_newb.bind("<Leave>", newl)
    employee_newb.bind("<Button-1>", newc)
    employee_newb.place(x=430, y=550)
    employee_deleteb = tkinter.Button(employee_window, state="disabled", text="حذف", font=("B nazanin", 16), bg="lightgreen")
    employee_deleteb.bind("<Enter>", deletee)
    employee_deleteb.bind("<Leave>", deletel)
    employee_deleteb.bind("<Button-1>", deletec)
    employee_deleteb.place(x=360, y=550)
    employee_editb = tkinter.Button(employee_window, state="disabled", text="ویرایش", font=("B nazanin", 16), bg="lightgreen")
    employee_editb.bind("<Enter>", edite)
    employee_editb.bind("<Leave>", editl)
    employee_editb.bind("<Button-1>", editc)
    employee_editb.place(x=275, y=550)
    employee_submitb = tkinter.Button(employee_window, state="disabled", text="ثبت اطلاعات", font=("B nazanin", 16), bg="lightgreen")
    employee_submitb.bind("<Enter>", submite)
    employee_submitb.bind("<Leave>", submitl)
    employee_submitb.bind("<Button-1>", submitc)
    employee_submitb.place(x=160, y=550)
    employee_searchb = tkinter.Button(employee_window, text="جستجو", font=("B nazanin", 16), bg="lightgreen")
    employee_searchb.bind("<Enter>", searche)
    employee_searchb.bind("<Leave>", searchl)
    employee_searchb.bind("<Button-1>", searchc)
    employee_searchb.place(x=80, y=550)
    employee_exitb = tkinter.Button(employee_window, text="خروج", font=("B nazanin", 16), bg="red")
    employee_exitb.bind("<Enter>", exite)
    employee_exitb.bind("<Leave>", exitl)
    employee_exitb.bind("<Button-1>", exitc)
    employee_exitb.place(x=10, y=570)
    # /Buttons
    employee_window.mainloop()
#func()