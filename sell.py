sumprice = 0
check_num = 0
submited = 0
from datetime import *
def func():
    import tkinter, sqlite3, win32ui
    import shamsidate
    from public1 import shop_money_unit, shopname, shoptype, shoptel, shopaddress
    from tkinter import StringVar
    from tkinter import messagebox
    from tkinter import ttk
    from shamsidate import sdate
    # printer
    # /printer
    connect = sqlite3.connect("mani_database.db")
    cursor = connect.cursor()

    def addbe(event):
        addb.config(bg='skyblue')
        sell_window.config(cursor="hand2")

    def addbl(event):
        addb.config(bg='lightgreen')
        sell_window.config(cursor="arrow")

    def addbc(event):
        code = sell_code.get()
        name = sell_name.get()
        price = sell_price.get()
        amount = sell_amount.get()
        allprice = sell_productallprice.get()
        if amount != "0" and amount != "":
            if code != "" and name != "" and price != "":
                legal_amount = cursor.execute("SELECT amount FROM product WHERE code="+str(code))
                legal_amount = list(legal_amount.fetchone())
                if legal_amount[0]>=int(amount):
                    tree.insert("", "end", values=([allprice, amount, price, name, code]))
                else:
                    unit = unitlabel.cget("text")
                    messagebox.showerror("خطا", ".کل موجودي اين کالا {0} {2} است. ولي شما تعداد فروش اين کالا را {1} {2} گذاشتيد لطفا توجه داشته باشید که تعداد فروش یک کالا باید همواره کمتر یا برابر با موجودی .آن باشد".format(str(legal_amount[0]), amount, unit))
            else:
                messagebox.showerror("خطا", "لطفا ابتدا یکی از کالا ها را از لیست کالا های موجود انتخاب کرده و بعد آن را به سبد .خرید اضافه کنید")
        else:
            messagebox.showerror("خطا", "لطفا مقدار/تعداد کالا را به درستی وارد کنید")
        global sumprice
        sumprice = 0
        for line in tree.get_children():
            sumprice += tree.item(line)['values'][0]
        sell_allprice.config(state="normal")
        sell_allprice.delete(0, "end")
        sell_allprice.insert(0, sumprice)
        sell_allprice.config(state="readonly")
        tree1.focus_force()


    def submitbe(event):
        submitb.config(bg='skyblue')
        sell_window.config(cursor="hand2")

    def submitbl(event):
        submitb.config(bg='lightgreen')
        sell_window.config(cursor="arrow")

    def submitbc(event):
        allprice = sell_allprice.get()
        off = sell_off.get()
        customer = sell_customer.get()
        if customer != "" and off != "":
            y = cursor.execute("SELECT name from customer WHERE code=" + customer)
            try:
                y = list(y.fetchone())
            except:
                messagebox.showerror("خطا",
                                     "کد مشتری وارد شده، معتبر نمی باشد. در صورتی که می خواهید از این کد استفاده کنید، باید ابتدا این مشتری را در بخش 'مشتریان' ثبت کرده و بعد اقدام به استفاده از .آن کنید")
            else:
                x = cursor.execute("SELECT MAX(code) FROM sell")
                lastcode = list(x.fetchone())
                if lastcode[0] == None:
                    lastcode[0] = 0
                for line in tree.get_children():
                    value = tree.item(line)['values']
                    cursor.execute(
                        "INSERT INTO soldproducts(sellcode,productcode,name,price,amount,allprice)VALUES({0},{1},'{2}' , {3}, {4}, {5})"
                            .format(lastcode[0] + 1, str(value[4]), str(value[3]), str(value[2]), str(value[1]),
                                    str(value[0])))
                    cursor.execute("UPDATE product SET amount=amount-{0} WHERE code={1}".format(str(value[1]),str(value[4])))
                cursor.execute(
                    "INSERT INTO sell(code,off,price,customer,customername,date,time)VALUES({0}, {1}, {2}, {3}, '{4}', '{5}', '{6}')".format(lastcode[0] + 1,int(off),int(allprice), int(customer), y[0],shamsidate.sdate, datetime.now().strftime("%H:%M:%S")))
                connect.commit()
                global submited
                submited = 1
                messagebox.showinfo("موفقیت", ".اطلاعات این فروش با کد {0} با موفقیت ثبت شدند".format(lastcode[0] + 1))
        else:
            messagebox.showerror("خطا", ".لطفا ابتدا تمامی بخش ها را پر کرده و بعد اقدام به ثبت اطلاعات این فروش کنید  \n نکته: در صورتی که مشتری را نمی شناسید، بخش کد مشتری را با کد  0 پر کنید و در صورتی هم که کالایتان تخفیفی ندارد، بخش تخفیف را با 0 پر کنید و هیچ کدام از .این دو بخش را خالی نگذارید")

    def printbe(event):
        printb.config(bg='skyblue')
        sell_window.config(cursor="hand2")

    def printbl(event):
        printb.config(bg='lightgreen')
        sell_window.config(cursor="arrow")

    def printbc(event):
        dc = win32ui.CreateDC()
        dc.CreatePrinterDC()
        dc.StartDoc('Mani software sell factor')
        dc.StartPage()
        dc.TextOut(2250,70, shoptype+" "+shopname)
        customer = sell_customer.get()
        y = cursor.execute("SELECT name from customer WHERE code=" + customer)
        try:
            y = list(y.fetchone())
        except:
            messagebox.showerror("خطا",
                                     "کد مشتری وارد شده، معتبر نمی باشد. در صورتی که می خواهید از این کد استفاده کنید، باید ابتدا این مشتری را در بخش 'مشتریان' ثبت کرده و بعد اقدام به استفاده از .آن کنید")
        else:
            x = cursor.execute("SELECT MAX(code) FROM sell")
            lastcode = list(x.fetchone())
            if lastcode[0] == None:
                lastcode[0] = 0
            if submited == 1:
                lastcode[0] -= 1
            if datetime.now().strftime("%H:%M:%S").find("11") == -1:
                dc.TextOut(3940, 220, "زمان: {0}".format(datetime.now().strftime("%H:%M:%S")))
            else:
                dc.TextOut(4300, 220, ":زمان")
                dc.TextOut(3930, 220, datetime.now().strftime("%H:%M:%S"))
            if sdate.find("11") == -1:
                dc.TextOut(2880, 220, "تاريخ: {0}".format(sdate))
            else:
                dc.TextOut(3300, 220, ":تاريخ")
                dc.TextOut(2830, 220, sdate)
            dc.TextOut(1530, 220, "مشتري: {0}".format(y[0]))
            if str(lastcode[0]+1).find("11") == -1:
                dc.TextOut(530, 220, "کد فروش: {0}".format(lastcode[0]+1))
            else:
                dc.TextOut(870, 220, ":کد فروش".format(lastcode[0]))
                dc.TextOut(530, 220, str(lastcode[0]+1))
            dc.TextOut(3900, 370, "کالا")
            dc.TextOut(2900, 370, "تعداد")
            dc.TextOut(1800, 370, "(قيمت واحد ({0}".format(shop_money_unit))
            dc.TextOut(800, 370, "(قيمت کل ({0}".format(shop_money_unit))
            product_height = 140
            dc.MoveTo(500, 480)
            dc.LineTo(4500, 480)
            dc.MoveTo(500, 340)
            dc.LineTo(4500, 340)
            for line in tree.get_children():
                value = tree.item(line)['values']
                dc.TextOut(3500, 370+product_height, str(value[3]))
                dc.TextOut(2700, 370+product_height, str(value[1]))
                dc.TextOut(1700, 370+product_height, str(value[2]))
                dc.TextOut(600, 370+product_height, str(value[0]))
                dc.MoveTo(500, 480+product_height)
                dc.LineTo(4500, 480+product_height)
                product_height += 140
            allprice = sell_allprice.get()
            off = sell_off.get()
            allprice_notoff = str(int(allprice)+int(off))
            if allprice_notoff.find("11") == -1:
                dc.TextOut(3500, 410+product_height, "مبلغ کل: {0} {1}".format(allprice_notoff, shop_money_unit))
            else:
                dc.TextOut(4200, 410+product_height, ":مبلغ کل")
                dc.TextOut(3580, 410+product_height, allprice_notoff)
                dc.TextOut(3400, 410+product_height, shop_money_unit)
            if off.find("11") == -1:
                dc.TextOut(2400, 410+product_height, "تخفيف: {0} {1}".format(off, shop_money_unit))
            else:
                dc.TextOut(2940, 410+product_height, ":تخفيف")
                dc.TextOut(2380, 410+product_height, off)
                dc.TextOut(2200, 410+product_height, shop_money_unit)
            if allprice.find("11") == -1:
                dc.TextOut(700, 410+product_height, "مبلغ قابل پرداخت: {0} {1}".format(allprice, shop_money_unit))
            else:
                dc.TextOut(1390, 410+product_height, ":مبلغ قابل پرداخت")
                dc.TextOut(780, 410+product_height, allprice)
                dc.TextOut(600, 410+product_height, shop_money_unit)
            dc.MoveTo(3400, 340)
            dc.LineTo(3400, 480+(product_height-140))
            dc.MoveTo(2600, 340)
            dc.LineTo(2600, 480+(product_height-140))
            dc.MoveTo(1600, 340)
            dc.LineTo(1600, 480+(product_height-140))
            dc.TextOut(2000, 560+product_height, "آدرس: {0}".format(shopaddress))
            if shoptel.find("11") == -1:
                dc.TextOut(600, 560+product_height, "شماره تلفن: {0}".format(shoptel))
            else:
                dc.TextOut(1200, 560+product_height, ":شماره تلفن")
                dc.TextOut(600, 560+product_height, shoptel)
            dc.EndPage()
            dc.EndDoc()


    def deletebe(event):
        deleteb.config(bg='skyblue')
        sell_window.config(cursor="hand2")

    def deletebl(event):
        deleteb.config(bg='lightgreen')
        sell_window.config(cursor="arrow")

    def deletebc(event):
        x = tree.get_children()
        try:
            selected_item = tree.selection()[0]
            tree.delete(selected_item)
        except IndexError:
            messagebox.showerror("خطا", "لطفا ابتدا یکی از کالا های موجود در سبد خرید را انتخاب کرده و بعد اقدام به حذف آن .کنید")

    def newbe(event):
        newb.config(bg='skyblue')
        sell_window.config(cursor="hand2")

    def newbl(event):
        newb.config(bg='lightgreen')
        sell_window.config(cursor="arrow")

    def newbc(event):
        global check_num
        check_num = 0
        global submited
        submited = 0
        sell_code.config(state="normal")
        sell_name.config(state="normal")
        sell_price.config(state="normal")
        sell_amount.config(state="normal")
        sell_productallprice.config(state="normal")
        sell_off.config(state="normal")
        sell_allprice.config(state="normal")
        sell_customer.config(state="normal")
        #c
        sell_code.delete(0, "end")
        sell_name.delete(0, "end")
        sell_price.delete(0, "end")
        sell_amount.delete(0, "end")
        sell_productallprice.delete(0, "end")
        sell_off.delete(0, "end")
        sell_allprice.delete(0, "end")
        sell_customer.delete(0, "end")
        sell_productallprice.insert(0, "0")
        sell_off.insert(0, "0")
        sell_allprice.insert(0, "0")
        sell_code.config(state="readonly")
        sell_name.config(state="readonly")
        sell_price.config(state="readonly")
        sell_allprice.config(state="readonly")
        sell_productallprice.config(state="readonly")
        sell_amount.config(state="normal")
        sell_customer.config(state="normal")
        sell_off.config(state="normal")
        sell_customer.insert(0, "0")
        sell_amount.focus()
        customer_name.config(text="مشتری ناشناس")
        unitlabel.config(text="واحد")
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        check_num = 1

    def exitbe(event):
        exitb.config(bg='skyblue')
        sell_window.config(cursor="hand2")

    def exitbl(event):
        exitb.config(bg='red')
        sell_window.config(cursor="arrow")

    def exitbc(event):
        sell_window.destroy()

    def tree_selected(event):
        selectedoption = list(tree1.item(tree1.focus())['values'])
        sell_code.config(state="normal")
        sell_name.config(state="normal")
        sell_price.config(state="normal")
        sell_productallprice.config(state="normal")
        sell_code.delete(0, "end")
        sell_name.delete(0, "end")
        sell_price.delete(0, "end")
        sell_amount.delete(0, "end")
        sell_productallprice.delete(0, "end")
        sell_productallprice.delete(0, "end")
        sell_price.insert(0, str(selectedoption[1]))
        sell_name.insert(0, str(selectedoption[2]))
        sell_code.insert(0, str(selectedoption[3]))
        sell_productallprice.insert(0, selectedoption[1])
        sell_amount.insert(0, "1")
        tree1.focus()
        sell_code.config(state="readonly")
        sell_name.config(state="readonly")
        sell_price.config(state="readonly")
        sell_productallprice.config(state="readonly")
        exe = cursor.execute("SELECT unit FROM product WHERE code="+str(selectedoption[3]))
        unit = list(exe.fetchone())
        unitlabel.config(text=unit[0])
    def tree_return(event):
        sell_amount.focus()

    def changefunction1():
        global check_num
        if check_num == 1 and sell_code.get() != "":
            code = sell_amount.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    sell_amount.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش تعداد کالا استفاده کنید، نه حروف")
            else:
                sell_productallprice.config(state="normal")
                sell_productallprice.delete(0, "end")
                price = int(sell_price.get())
                sell_productallprice.insert(0, str(int(code)*price))
                sell_productallprice.config(state="readonly")

    def changefunction2():
        global check_num
        if check_num == 1:
            code = sell_off.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    sell_off.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش تخفیف استفاده کنید، نه حروف")
                else:
                    sell_allprice.config(state="normal")
                    sell_allprice.delete(0, "end")
                    sell_allprice.insert(0, sumprice)
                    sell_allprice.config(state="readonly")
            else:
                sell_allprice.config(state="normal")
                sell_allprice.delete(0, "end")
                sell_allprice.insert(0, str(sumprice-int(code)))
                sell_allprice.config(state="readonly")

    def changefunction3():
        global check_num
        if check_num == 1:
            code = sell_customer.get()
            try:
                int(code)
            except:
                if code != "":
                    codelength = len(code)
                    check_num = 0
                    sell_customer.delete(codelength - 1, "end")
                    check_num = 1
                    messagebox.showwarning("خطا", "شما تنها می توانید از اعداد در بخش کد مشتری استفاده کنید، نه حروف")
            else:
                customercode = cursor.execute("SELECT name FROM customer WHERE code="+code)
                try:
                    customercode = list(customercode.fetchone())
                except:
                    customer_name.place(x=613, y=380)
                    customer_name.config(text="کد مشتري نامعتبر است", fg="red")
                else:
                    if len(customercode[0])>=20 and len(customercode[0])<=24:
                        customer_name.place(x=600, y=380)
                    elif len(customercode[0])>=25:
                        customer_name.place(x=585, y=380)
                    else:
                        customer_name.place(x=630, y=380)
                    customer_name.config(text=customercode[0], fg="black")

    sell_window = tkinter.Tk()
    sell_window.geometry("890x480")
    sell_window.resizable(0, 0)
    sell_window.title("فروش")
    sell_window.iconbitmap(r"images\window_icon.ico")
    sell_window.focus_force()
    # labels
    tkinter.Label(sell_window, text="فروش", font=("B Nazanin", 25), fg="orangered").pack()
    tkinter.Label(sell_window, text=":کد کالا", font=("B Nazanin", 16)).place(x=800, y=40)
    tkinter.Label(sell_window, text=":نام کالا", font=("B Nazanin", 16)).place(x=800, y=80)
    tkinter.Label(sell_window, text=":قیمت واحد", font=("B Nazanin", 16)).place(x=800, y=120)
    tkinter.Label(sell_window, text=":تعداد/مقدار", font=("B Nazanin", 16)).place(x=800, y=165)
    tkinter.Label(sell_window, text=":قیمت کل", font=("B Nazanin", 16)).place(x=800, y=210)
    tkinter.Label(sell_window, text=shop_money_unit, font=("B Nazanin", 16)).place(x=630, y=125)
    tkinter.Label(sell_window, text=shop_money_unit, font=("B Nazanin", 16)).place(x=630, y=338)
    tkinter.Label(sell_window, text=shop_money_unit, font=("B Nazanin", 16)).place(x=630, y=298)
    tkinter.Label(sell_window, text=shop_money_unit, font=("B Nazanin", 16)).place(x=630, y=210)
    unitlabel = tkinter.Label(sell_window, text="واحد", font=("B Nazanin", 14))
    unitlabel.place(x=630, y=165)
    tkinter.Label(sell_window, text=":تخفیف", font=("B Nazanin", 16)).place(x=800, y=300)
    tkinter.Label(sell_window, text=":مبلغ کل", font=("B Nazanin", 16)).place(x=800, y=338)
    tkinter.Label(sell_window, text=":کد مشتری", font=("B Nazanin", 16)).place(x=800, y=375)
    tkinter.Label(sell_window, text=":سبد خرید", font=("B Nazanin", 16)).place(x=548, y=40)
    tkinter.Label(sell_window, text=":لیست کالا های موجود", font=("B Nazanin", 16)).place(x=140, y=40)
    customer_name = tkinter.Label(sell_window, text="مشتري ناشناس", font=("B Nazanin", 11))
    customer_name.place(x=630, y=380)
    # /labels
    # buttons
    addb = tkinter.Button(sell_window, text='افزودن به سبد خرید', width=17, font=("", 18), bg="lightgreen")
    addb.bind("<Enter>", addbe)
    addb.bind("<Leave>", addbl)
    addb.bind("<Button-1>", addbc)
    addb.place(x=630, y=250)
    submitb = tkinter.Button(sell_window, text='ثبت', width=7, font=("", 18), bg="lightgreen")
    submitb.bind("<Enter>", submitbe)
    submitb.bind("<Leave>", submitbl)
    submitb.bind("<Button-1>", submitbc)
    submitb.place(x=770, y=420)
    printb = tkinter.Button(sell_window, text='چاپ فاکتور', width=8, font=("", 18), bg="lightgreen")
    printb.bind("<Enter>", printbe)
    printb.bind("<Leave>", printbl)
    printb.bind("<Button-1>", printbc)
    printb.place(x=630, y=420)
    newb = tkinter.Button(sell_window, text='جدید', width=7, font=("", 20), bg="lightgreen")
    newb.bind("<Enter>", newbe)
    newb.bind("<Leave>", newbl)
    newb.bind("<Button-1>", newbc)
    newb.place(x=460, y=380)
    deleteb = tkinter.Button(sell_window, text='حذف', width=7, font=("", 20), bg="lightgreen")
    deleteb.bind("<Enter>", deletebe)
    deleteb.bind("<Leave>", deletebl)
    deleteb.bind("<Button-1>", deletebc)
    deleteb.place(x=320, y=380)
    exitb = tkinter.Button(sell_window, text='خروج', width=5, font=("", 18), bg="red")
    exitb.bind("<Enter>", exitbe)
    exitb.bind("<Leave>", exitbl)
    exitb.bind("<Button-1>", exitbc)
    exitb.place(x=8, y=425)
    # /buttons
    # entries
    sv1 = StringVar()
    sv1.trace("w", lambda name, index, mode, sv=sv1: changefunction1())
    sv2 = StringVar()
    sv2.trace("w", lambda name, index, mode, sv=sv2: changefunction2())
    sv3 = StringVar()
    sv3.trace("w", lambda name, index, mode, sv=sv3: changefunction3())
    sell_code = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, state="readonly")
    sell_code.place(x=630, y=45)
    sell_name = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, state="readonly")
    sell_name.place(x=630, y=85)
    sell_price = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=14, state="readonly")
    sell_price.place(x=677, y=125)
    sell_amount = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=8, textvariable=sv1)
    sell_amount.place(x=725, y=165)
    sell_amount.bind("<Return>", addbc)
    sell_off = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=14, textvariable=sv2)
    sell_off.insert(0, "0")
    sell_off.place(x=677, y=305)
    sell_customer = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=7, textvariable=sv3)
    sell_customer.place(x=733, y=380)
    sell_customer.insert(0, "0")
    sell_allprice = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=14)
    sell_allprice.place(x=677, y=343)
    sell_allprice.insert(0, "0")
    sell_allprice.config(state="readonly")
    sell_productallprice = tkinter.Entry(sell_window, font=("B nazanin", 13), justify=tkinter.RIGHT, width=14, state="readonly")
    sell_productallprice.place(x=677, y=212)
    global check_num
    check_num = 1
    # /entries
    # product tree
    tree = ttk.Treeview(sell_window, height=13)
    tree.place(x=300, y=80)
    tree["columns"] = ("1", "2", "3", "4", "5")
    tree['show'] = 'headings'
    tree.column("1", width=55, anchor='c')
    tree.column("2", width=33, anchor='c')
    tree.column("3", width=55, anchor='c')
    tree.column("4", width=90, anchor='c')
    tree.column("5", width=85, anchor='c')
    tree.heading("1", text="قیمت کل")
    tree.heading("2", text="مقدار")
    tree.heading("3", text="قیمت")
    tree.heading("4", text="نام کالا")
    tree.heading("5", text="کد کالا")
    tree1 = ttk.Treeview(sell_window, height=13)
    tree1.place(x=10, y=80)
    tree1["columns"] = ("1", "2", "3", "4")
    tree1['show'] = 'headings'
    tree1.column("1", width=50, anchor='c')
    tree1.column("2", width=55, anchor='c')
    tree1.column("3", width=90, anchor='c')
    tree1.column("4", width=85, anchor='c')
    tree1.heading("1", text="موجودی")
    tree1.heading("2", text="قیمت")
    tree1.heading("3", text="نام کالا")
    tree1.heading("4", text="کد کالا")
    e = cursor.execute("SELECT code,name,sellprice,amount FROM product WHERE amount>0")
    productlist = list(e.fetchall())
    for i in productlist:
        product = list(i)
        product.reverse()
        tree1.insert("", "end", values=(product))
    tree1.bind("<<TreeviewSelect>>", tree_selected)
    tree1.bind("<Return>", tree_return)
    tree1.focus()
    # /product tree
    sell_window.mainloop()


#func()
