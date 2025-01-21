employee_selected = []
check_num = 0


def func():
    import tkinter, sqlite3
    from tkinter import messagebox
    from tkinter import StringVar
    from public1 import shop_money_unit
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
            employee_code.config(state="normal")
            result = cursor.execute("SELECT max(code) FROM employees")
            row = list(result.fetchone())
            if row[0] == None:
                row[0] = 0
            employee_code.delete(0, "end")
            employee_name.delete(0, "end")
            employee_lastname.delete(0, "end")
            employee_tel.delete(0, "end")
            employee_details.delete("1.0", "end")
            employee_address.delete(0, "end")
            employee_salary.delete(0, "end")
            employee_birth.delete(0, "end")
            employee_job.delete(0, "end")
            employee_code.insert(0, str(row[0]+1))
            employee_newb.config(state="normal")
            employee_deleteb.config(state="disabled")
            employee_editb.config(state="disabled")
            employee_submitb.config(state="normal")
            employee_code.config(state="normal")
            employee_code.focus()
    def deletec(event):
        if employee_deleteb.cget("state") == "normal":
            code = employee_code.get()
            if code != "":
                try:
                    cursor.execute("DELETE FROM employees WHERE code=" + code)
                    connect.commit()
                except:
                    messagebox.showerror("خطا", "!اطلاعات این کارکن حذف نشدند")
                else:
                    messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت حذف شدند")

    def editc(event):
        if employee_editb.cget("state") == "normal":
            code = employee_code.get()
            name = employee_name.get()
            lastname = employee_lastname.get()
            tel = employee_tel.get()
            details = employee_details.get("1.0", "end")
            address = employee_address.get()
            salary = employee_salary.get()
            birth = employee_birth.get()
            job = employee_job.get()
            if code != "":
                try:
                    cursor.execute("UPDATE employees SET name='{0}', lastname='{1}', tel='{2}',"
                                   "address='{3}', birth='{4}', job='{5}', salary='{6}',  details='{7}'  WHERE code={8}".format(
                        name, lastname, tel, address, birth, job, salary, details, int(code)))
                    connect.commit()
                except:
                    messagebox.showerror("خطا", "!اطلاعات این کارکن ویرایش نشدند")
                else:
                    messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت ویرایش شدند")

    def submitc(event):
        if employee_submitb.cget("state") == "normal":
            name = employee_name.get()
            lastname = employee_lastname.get()
            tel = employee_tel.get()
            details = employee_details.get("1.0", "end")
            address = employee_address.get()
            salary = employee_salary.get()
            birth = employee_birth.get()
            job = employee_job.get()
            code = employee_code.get()
            if name != "" and lastname != "" and job != "" and code != "":
                cursor.execute("INSERT INTO employees(name,lastname,tel,address,birth,job,salary,details,code)"
                               "VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}', {8})".format(
                                name, lastname, tel, address, birth, job, salary, details, code))
                connect.commit()
                messagebox.showinfo("موفقیت", ".اطلاعات با موفقیت ثبت شدند")
                employee_newb.config(state="normal")
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
            global employee_selected
            employee_selected = selected
            employee_code.config(state="normal")
            employee_code.delete(0, "end")
            employee_name.delete(0, "end")
            employee_lastname.delete(0, "end")
            employee_tel.delete(0, "end")
            employee_details.delete("1.0", "end")
            employee_address.delete(0, "end")
            employee_salary.delete(0, "end")
            employee_birth.delete(0, "end")
            employee_job.delete(0, "end")
            employee_selected.reverse()
            employee_code.insert(0, employee_selected[0])
            employee_name.insert(0, employee_selected[1])
            employee_lastname.insert(0, employee_selected[2])
            employee_tel.insert(0, str(employee_selected[3]))
            employee_address.insert(0, employee_selected[4])
            employee_birth.insert(0, employee_selected[5])
            employee_salary.insert(0, employee_selected[6])
            employee_job.insert(0, employee_selected[7])
            employee_details.insert("0.5", employee_selected[8])
            employee_deleteb.config(state="normal")
            employee_editb.config(state="normal")
            employee_code.config(state="readonly")
            employee_search_window.destroy()

        employee_search_window = tkinter.Tk()
        employee_search_window.resizable(0, 0)
        employee_search_window.title("جستجو ی کارکنان")
        employee_search_window.iconbitmap(r"images\window_icon.ico")
        employee_search_window.focus_force()
        tkinter.Label(employee_search_window,
                      text="کلیک کنید" + " Enter " + "جهت انتخاب یکی از کارکنان، بعد از از انتخاب آن، روی دکمه ی ",
                      font=("B nazanin", 13)).pack()
        tree = ttk.Treeview(employee_search_window, height=15)
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
        tree.heading("2", text="سمت")
        tree.heading("3", text="حقوق")
        tree.heading("4", text="تاریخ تولد")
        tree.heading("5", text="آدرس")
        tree.heading("6", text="شماره تلفن")
        tree.heading("7", text="نام خانوادگی")
        tree.heading("8", text="نام")
        tree.heading("9", text="کد")
        # values
        e = cursor.execute("SELECT * FROM employees")
        employeelist = list(e.fetchall())
        for i in employeelist:
            employee = list(i)
            employee.reverse()
            tree.insert("", "end", values=(employee))
        employee_search_window.bind("<Return>", select_employee)
        employee_search_window.mainloop()
        # end
    def changefunction1():
        global check_num
        if check_num == 1:
            code = employee_code.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    employee_code.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش کد کارکنان استفاده کنید، نه حروف")

    def changefunction2():
        global check_num
        if check_num == 1:
            code = employee_salary.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    employee_salary.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش حقوق کارکنان استفاده کنید، نه حروف")

    employee_window = tkinter.Tk()
    employee_window.geometry("500x640")
    employee_window.resizable(0, 0)
    employee_window.title("اطلاعات کارکنان")
    employee_window.iconbitmap(r"images\window_icon.ico")
    employee_window.focus_force()
    # labels
    tkinter.Label(employee_window, font=("B nazanin", 25), fg="orangered", text="اطلاعات کارکنان").pack()
    tkinter.Label(employee_window, font=("", 17), text=":(*)کد ").place(x=360, y=50)
    tkinter.Label(employee_window, font=("", 17), text=":(*)نام ").place(x=360, y=100)
    tkinter.Label(employee_window, font=("", 17), text=":(*)نام خانوادگی").place(x=360, y=150)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":شماره تلفن").place(x=360, y=200)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":آدرس").place(x=360, y=250)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":تاریخ تولد").place(x=360, y=300)
    tkinter.Label(employee_window, font=("", 17), text=":(*)سِمَت").place(x=360, y=350)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":حقوق").place(x=360, y=400)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=":توضیحات").place(x=360, y=450)
    tkinter.Label(employee_window, font=("B nazanin", 20), text=shop_money_unit).place(x=115, y=400)
    # /labels
    # Entries and texts
    sv1 = StringVar()
    sv1.trace("w", lambda name, index, mode, sv=sv1: changefunction1())
    sv2 = StringVar()
    sv2.trace("w", lambda name, index, mode, sv=sv2: changefunction2())
    employee_code = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT, state="readonly", textvariable=sv1)
    employee_code.place(x=170, y=55)
    employee_name = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    employee_name.place(x=170, y=105)
    employee_lastname = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    employee_lastname.place(x=170, y=155)
    employee_tel = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    employee_tel.place(x=170, y=205)
    employee_address = tkinter.Entry(employee_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=43)
    employee_address.place(x=10, y=255)
    employee_birth = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    employee_birth.place(x=170, y=305)
    employee_job = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT)
    employee_job.place(x=170, y=355)
    employee_salary = tkinter.Entry(employee_window, font=("B nazanin", 15), justify=tkinter.RIGHT, textvariable=sv2)
    employee_salary.place(x=170, y=405)
    employee_details = tkinter.Text(employee_window, font=("B nazanin", 13), height=3, width=43)
    employee_details.place(x=10, y=455)
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
    global check_num
    check_num = 1
    # /Buttons
    employee_window.mainloop()
#func()