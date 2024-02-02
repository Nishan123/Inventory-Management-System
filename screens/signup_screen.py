from tkinter import *
from tkinter import font

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)



# creating a icon path
icon_path = "assets/stockpanda1.ico"

# using iconpath
root.iconbitmap(icon_path)


# icon_image path
callImg = PhotoImage(file='assets/telephone.png')
eyeImg = PhotoImage(file='assets/eye_view_icon.png')
eyeSlashImg = PhotoImage(file='assets/eye_slash_icon.png')


def password_visibility():
    if password.cget('show') == '*':
        password.config(show="")
        eye_label.config(image=eyeImg)
    else:
        password.config(show="*")
        eye_label.config(image=eyeSlashImg)


def confirm_password_visibility():
    if confirmPassword.cget('show') == '*':
        confirmPassword.config(show="")
        eye_label_2.config(image=eyeImg)
    else:
        confirmPassword.config(show="*")
        eye_label_2.config(image=eyeSlashImg)


def alreadyHaveAccount():
    root.destroy()
    import login_screen


def PhoneOnEnter(e):
    phone.delete(0, "end")


def PhoneOnLeave(e):
    phoneData = phone.get()
    if phoneData == "":
        phone.insert(0, "  Phone Number")


def PassOnEnter(e):
    password.delete(0, "end")


def PassOnLeave(e):
    passwordData = password.get()
    if passwordData == "":
        password.insert(0, "  Password")


def ConfPassOnEnter(e):
    confirmPassword.delete(0, "end")


def ConfPassOnLeave(e):
    confPasswordData = confirmPassword.get()
    if confPasswordData == "":
        confirmPassword.insert(0, "  Confirm Password")


# Custom text styles
customButtonFont = font.Font(size=16, weight="bold")
customTitleFont = font.Font(size=20, weight="bold")

# for hero text
Label(root, text="Stock Panda", bg="#8A908B", font=(
    "Arial", 30, "bold"), fg="white").place(x=30, y=290)
Label(root, text="Some Description about the software", bg="#8A908B",
      font=("Arial", 20), fg="white").place(x=30, y=340)

# to display text logo
textlogo = PhotoImage(file="assets/textlogo.png")
logoDispaly = Label(root, image=textlogo, bg="#8A908B")
logoDispaly.place(x=30, y=20)

container = Frame(bg="#D9D9D9", height=700, width=450)
container.pack_propagate(False)
container.pack(side=RIGHT)

# to display image logo
imageLogo = PhotoImage(file="assets/imagelogo.png")
logoDispaly = Label(container, image=imageLogo, bg="#D9D9D9")
logoDispaly.place(x=150, y=50)

# Welcome text
h1 = Label(container, text="Create an Account",
           bg="#D9D9D9", font=customTitleFont)
h1.place(x=120, y=230)

# for text fields
phone = Entry(container, width=33, font=(10))
phone.insert(0, "  Phone Number")
phone.bind("<FocusIn>", PhoneOnEnter)
phone.bind("<FocusOut>", PhoneOnLeave)
phone.place(x=90, y=300, height=38)

password = Entry(container, width=33, font=(10))
password.insert(0, "  Password")
password.bind("<FocusIn>", PassOnEnter)
password.bind("<FocusOut>", PassOnLeave)
password.place(x=90, y=350, height=38)

confirmPassword = Entry(container, width=33, font=(10))
confirmPassword.insert(0, "  Confirm Password")
confirmPassword.bind("<FocusIn>", ConfPassOnEnter)
confirmPassword.bind("<FocusOut>", ConfPassOnLeave)
confirmPassword.place(x=90, y=400, height=38)

# icon label_call
icon_label_call = Label(root, image=callImg, cursor='hand2')
icon_label_call.place(in_=phone, relx=1.0, rely=0.0, anchor='ne')

# icon label eye and eyeslash for password
eye_label = Label(root, image=eyeImg, cursor='hand2')
eye_label.place(in_=password, relx=1.0, rely=0.0, anchor='ne')
eye_label.bind("<Button-1>", lambda event: password_visibility())


# # icon label eye and eyeslash for confirm password
eye_label_2 = Label(root, image=eyeImg, cursor='hand2')
eye_label_2.place(in_=confirmPassword, relx=1.0, rely=0.0, anchor='ne')
eye_label_2.bind("<Button-1>", lambda event: confirm_password_visibility())


# for login button
login = Button(container, text="Log in", height=1, width=22,
               border=0, bg="#FF5252", fg="white", font=customButtonFont)
login.place(x=96, y=520)

# already have an account button
signUp = Button(container, text="Already have an account", border=0, fg="blue", bg="#D9D9D9", font=1,
                command=alreadyHaveAccount)
signUp.place(x=130, y=650)

root.mainloop()
