import tkinter
code = ["1sa", "lke", "qw", "bw", "2hg", "l7d", "zqy", "sa8", "c", "i", "qw6", "elz", ":;x", "zym", "xpw", "sk",
        "prv", "v@h", "vl$", "b%1", "s", "%mo", "b}3", "mz", "7%.", "b-z", ".u8", "vw", "sut", "a9d", "vul", "/0j",
        "lwg", "r", "by", "8.?", "qkw", "bue", "7@", "#e", "0x", "p#s", "nek", "3*m", "mqo", "bvc", "o", "d$",
        "q:z", "b/2", "4*x", "z#2", "xts", "l?g", "s}"]
y = "ابپتثجچحخدذرزژسشصضطظعغقفکگلمنوه ی.?!:;/\@#&*)(}{][-+$%'"


def encrypt(event):
    normal = str(normal_text.get("1.0", "end"))
    i = 0
    for x in y:
        normal = str(normal.replace(x, code[i]))
        i += 1
    encrypted_text.delete("1.0", "end")
    encrypted_text.insert("1.0", normal)


def decrypt(event):
    encrypted = str(encrypted_text.get("1.0", "end"))
    i = 0
    for x in code:
        encrypted = str(encrypted.replace(x,y[i]))
        i += 1
    normal_text.delete("1.0", "end")
    normal_text.insert("1.0", encrypted)


window = tkinter.Tk()
window.resizable(0, 0)
window.title("رمز نگاری")
window.config(bg="black")
window.geometry("500x500")
tkinter.Label(text="نرم افزار رمزنگاری مانی", font=("B nazanin", 20), fg="red",bg="black").pack()
tkinter.Label(text=":متن اصلی", font=("B nazanin", 15),bg="black", fg="red").pack()
normal_text = tkinter.Text(height=5, font=("B nazanin", 15),bg="black", fg="white")
normal_text.pack()
tkinter.Label(text=":متن رمز گذاری شده", font=("B nazanin", 15),bg="black", fg="red").pack()
encrypted_text = tkinter.Text(height=5, font=("", 15), bg="black", fg="white")
encrypted_text.pack()
encryptb = tkinter.Button(text="رمز گذاری", bg="blue", fg="white")
encryptb.place(x=300, y=450)
encryptb.bind("<Button-1>", encrypt)
decryptb = tkinter.Button(text="رمز گشایی", bg="blue", fg="white")
decryptb.place(x=200, y=450)
decryptb.bind("<Button-1>", decrypt)
window.mainloop()
