def func():
    import tkinter, sqlite3
    from tkinter import ttk
    import employee_info
    connect = sqlite3.connect("mani_database.db")
    cursor = connect.cursor()
# as

    def select_employee(event):
        selected = list(tree.item(tree.focus())['values'])
        employee_info.employee_selected = selected
        employee_info.x = 2
        employee_search_window.destroy()

    def employee_search_exitc(event):
        employee_search_window.destroy()

    def employee_search_exite(event):
        employee_search_exit.config(bg="skyblue")
        employee_search_window.config(cursor="hand2")

    def employee_search_exitl(event):
        employee_search_exit.config(bg="lightgreen")
        employee_search_window.config(cursor="arrow")

    employee_search_window = tkinter.Tk()
    employee_search_window.resizable(0, 0)
    employee_search_window.title("جستجو ی کارکنان")
    employee_search_window.iconbitmap(r"images\window_icon.ico")
    tkinter.Label(employee_search_window, text="کلیک کنید"+" enter "+"جهت انتخاب یکی از کارکنان، بعد از از انتخاب آن، روی دکمه ی ", font=("B nazanin",13)).pack()
    tree = ttk.Treeview(employee_search_window,height=10)
    tree.pack()
    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
    tree['show'] = 'headings'
    tree.column("1", width=150, anchor='c')
    tree.column("2", width=90, anchor='c')
    tree.column("3", width=90, anchor='c')
    tree.column("4", width=90, anchor='c')
    tree.column("5", width=150, anchor='c')
    tree.column("6", width=90, anchor='c')
    tree.column("7", width=90, anchor='c')
    tree.column("8", width=90, anchor='c')
    tree.heading("1", text="توضیحات")
    tree.heading("2", text="سمت")
    tree.heading("3", text="حقوق")
    tree.heading("4", text="تاریخ تولد")
    tree.heading("5", text="آدرس")
    tree.heading("6", text="شماره تلفن")
    tree.heading("7", text="نام خانوادگی")
    tree.heading("8", text="نام")
    # values
    e = cursor.execute("SELECT * FROM employees")
    employeelist = list(e.fetchall())
    for i in employeelist:
        employee = list(i)
        employee.reverse()
        tree.insert("", "end", values=(employee))
    employee_search_exit = tkinter.Button(employee_search_window, text="خروج", font=("B nazanin", 16), bg="red")
    employee_search_exit.bind("<Enter>", employee_search_exite)
    employee_search_exit.bind("<Leave>", employee_search_exitl)
    employee_search_exit.bind("<Button-1>", employee_search_exitc)
    employee_search_exit.pack()
    employee_search_window.bind("<Return>", select_employee)
    employee_search_window.mainloop()

#func()
