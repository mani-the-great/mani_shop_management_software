def func():
    import tkinter, sqlite3
    from tkinter import messagebox
    from public1 import shop_money_unit
    connect = sqlite3.connect("mani_database.db")
    cursor = connect.cursor()

    def make_reporte(event):
        make_reportb.config(bg='skyblue')
        report_window.config(cursor="hand2")

    def make_reportl(event):
        make_reportb.config(bg='lightgreen')
        report_window.config(cursor="arrow")

    def new_reporte(event):
        new_reportb.config(bg='skyblue')
        report_window.config(cursor="hand2")

    def new_reportl(event):
        new_reportb.config(bg='lightgreen')
        report_window.config(cursor="arrow")

    def new_reportc(event):
        from_code.delete(0, "end")
        from_off.delete(0, "end")
        from_price.delete(0, "end")
        from_customer.delete(0, "end")
        to_code.delete(0, "end")
        to_off.delete(0, "end")
        to_price.delete(0, "end")
        to_customer.delete(0, "end")
        from_code.focus()

    def make_reportc(event):
        from_codev = from_code.get()
        from_offv = from_off.get()
        from_pricev = from_price.get()
        from_customerv = from_customer.get()
        to_codev = to_code.get()
        to_offv = to_off.get()
        to_pricev = to_price.get()
        to_customerv = to_customer.get()
        reportlist = cursor.execute("SELECT MAX(code),MAX(off),MAX(price),MAX(customer) FROM sell")
        reportlist = list(reportlist.fetchone())
        if to_codev == "":
            if from_codev == "":
                from_codev = "0"
                to_codev = str(reportlist[0])
            else:
                to_codev = from_codev
        if to_offv == "":
            if from_offv == "":
                from_offv = "0"
                to_offv = str(reportlist[1])
            else:
                to_offv = from_offv
        if to_pricev == "":
            if from_pricev == "":
                from_pricev = "0"
                to_pricev = str(reportlist[2])
            else:
                to_pricev = from_pricev
        if to_customerv == "":
            if from_customerv == "":
                from_customerv = "0"
                to_customerv = str(reportlist[3])
            else:
                to_customerv = from_customerv
        reportlist = cursor.execute("SELECT * FROM sell where code>={0} AND off>={1} AND price>={2} AND customer>={3}"
                                    " AND code<={4} AND off<={5} AND price<={6} AND customer<={7}".format(
                                     from_codev, from_offv, from_pricev, from_customerv, to_codev, to_offv, to_pricev, to_customerv))
        reportlist = list(reportlist.fetchall())
        # start
        from tkinter import ttk

        # as

        def select_employee(event):
            selected = list(tree.item(tree.focus())['values'])
            global employee_selected
            employee_selected = selected
            # start sell items

            def select_employee(event):
                selected = list(tree1.item(tree1.focus())['values'])
                global employee_selected
                employee_selected = selected


            employee_search_window = tkinter.Tk()
            employee_search_window.resizable(0, 0)
            try:
                employee_search_window.title("لیست کالا های فروخته شده در فروش شماره {0}".format(employee_selected[6]))
            except:
                messagebox.showwarning("خطا","لطفا ابتدا از فهرست فروش ها یکی از فروش ها را انتخاب کرده و بعد اقدام به دیدن .لیست کالا های فروخته شده در آن فروش کنید")
                employee_search_window.destroy()
            employee_search_window.iconbitmap(r"images\window_icon.ico")
            employee_search_window.focus_force()
            tkinter.Label(employee_search_window, text=":لیست کالا های فروخته شده در فروش شماره {0}".format(employee_selected[6]), font=("B nazanin", 13)).pack()
            tree1 = ttk.Treeview(employee_search_window, height=15)
            tree1.pack()
            tree1["columns"] = ("1", "2", "3", "4", "5")
            tree1['show'] = 'headings'
            tree1.column("1", width=100, anchor='c')
            tree1.column("2", width=60, anchor='c')
            tree1.column("3", width=90, anchor='c')
            tree1.column("4", width=150, anchor='c')
            tree1.column("5", width=90, anchor='c')
            tree1.heading("1", text="قیمت کل")
            tree1.heading("2", text="تعداد")
            tree1.heading("3", text="قیمت واحد")
            tree1.heading("4", text="نام کالا")
            tree1.heading("5", text="کد کالا")
            # values
            sellcode = employee_selected[6]
            selllist = cursor.execute("SELECT * FROM soldproducts WHERE sellcode="+str(sellcode))
            selllist = list(selllist.fetchall())
            for i in selllist:
                employee = list(i)
                employee.reverse()
                tree1.insert("", "end", values=(str(employee[0]), str(employee[1]), str(employee[2]),str(employee[3]),str(employee[4])))
            employee_search_window.bind("<Return>", select_employee)
            employee_search_window.mainloop()
            # /start sell items

        employee_search_window = tkinter.Tk()
        employee_search_window.resizable(0, 0)
        employee_search_window.title("گزارش فروش")
        employee_search_window.iconbitmap(r"images\window_icon.ico")
        employee_search_window.focus_force()
        tkinter.Label(employee_search_window,
                      text="کلیک کنید" + " Enter " + "جهت مشاهده لیست کالا های فروخته شده در هر فروش، پس از انتخاب آن روی دکمه ی  ",
                      font=("B nazanin", 13)).pack()
        tree = ttk.Treeview(employee_search_window, height=25)
        tree.pack()
        tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        tree['show'] = 'headings'
        tree.column("1", width=70, anchor='c')
        tree.column("2", width=70, anchor='c')
        tree.column("3", width=150, anchor='c')
        tree.column("4", width=90, anchor='c')
        tree.column("5", width=150, anchor='c')
        tree.column("6", width=110, anchor='c')
        tree.column("7", width=90, anchor='c')
        tree.heading("1", text="زمان")
        tree.heading("2", text="تاریخ")
        tree.heading("3", text="نام مشتری")
        tree.heading("4", text="کد مشتری")
        tree.heading("5", text="مبلغ کل")
        tree.heading("6", text="تخفیف")
        tree.heading("7", text="کد فروش")
        # values
        for i in reportlist:
            employee = list(i)
            employee.reverse()
            tree.insert("", "end", values=employee)
        employee_search_window.bind("<Return>", select_employee)
        employee_search_window.mainloop()
        # end

    def exit_reporte(event):
        exit_reportb.config(bg='skyblue')
        report_window.config(cursor="hand2")

    def exit_reportl(event):
        exit_reportb.config(bg='red')
        report_window.config(cursor="arrow")

    def exit_reportc(event):
        report_window.destroy()

    report_window = tkinter.Tk()
    report_window.geometry("500x360")
    report_window.resizable(0, 0)
    report_window.title("گزارش فروش")
    report_window.iconbitmap(r"images\window_icon.ico")
    report_window.focus_force()
    # labels
    tkinter.Label(report_window, text="گزارشات", font=("B Nazanin", 20), fg="orangered").pack()
    tkinter.Label(report_window, text=" کد فروش: از", font=("B Nazanin", 15)).place(x=400, y=100)
    tkinter.Label(report_window, text=" تخفیف: از", font=("B Nazanin", 15)).place(x=400, y=150)
    tkinter.Label(report_window, text=" مبلغ کل: از", font=("B Nazanin", 15)).place(x=400, y=200)
    tkinter.Label(report_window, text=" کد مشتری: از", font=("B Nazanin", 15)).place(x=400, y=250)
    tkinter.Label(report_window, text="تا", font=("B Nazanin", 15)).place(x=270, y=100)
    tkinter.Label(report_window, text="تا", font=("B Nazanin", 15)).place(x=270, y=150)
    tkinter.Label(report_window, text="تا", font=("B Nazanin", 15)).place(x=270, y=200)
    tkinter.Label(report_window, text="تا", font=("B Nazanin", 15)).place(x=270, y=250)
    tkinter.Label(report_window, text=shop_money_unit, font=("B Nazanin", 15)).place(x=110, y=150)
    tkinter.Label(report_window, text=shop_money_unit, font=("B Nazanin", 15)).place(x=110, y=200)
    # /labels
    # entries
    from_code = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    from_code.place(x=290, y=100)
    from_off = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    from_off.place(x=290, y=150)
    from_price = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    from_price.place(x=290, y=200)
    from_customer = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    from_customer.place(x=290, y=250)
    to_code = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    to_code.place(x=155, y=100)
    to_off = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    to_off.place(x=155, y=150)
    to_price = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    to_price.place(x=155, y=200)
    to_customer = tkinter.Entry(report_window, font=("B Nazanin", 15), width=12)
    to_customer.place(x=155, y=250)
    from_code.focus()
    # /entries
    # buttons
    make_reportb = tkinter.Button(report_window, text="تهیه گزارش", font=("", 18), bg="lightgreen", width=8)
    make_reportb.bind("<Enter>", make_reporte)
    make_reportb.bind("<Leave>", make_reportl)
    make_reportb.bind("<Button-1>", make_reportc)
    make_reportb.place(x=120, y=300)
    exit_reportb = tkinter.Button(report_window, text="خروج", font=("", 18), bg="red", width=7)
    exit_reportb.bind("<Enter>", exit_reporte)
    exit_reportb.bind("<Leave>", exit_reportl)
    exit_reportb.bind("<Button-1>", exit_reportc)
    exit_reportb.place(x=5, y=300)
    new_reportb = tkinter.Button(report_window, text="جدید", font=("", 18), bg="lightgreen", width=7)
    new_reportb.bind("<Enter>", new_reporte)
    new_reportb.bind("<Leave>", new_reportl)
    new_reportb.bind("<Button-1>", new_reportc)
    new_reportb.place(x=250, y=300)
    # /buttons
    report_window.mainloop()


#func()
