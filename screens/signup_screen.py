from tkinter import *
from tkinter import font

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)

# Custom text styles
customButtonFont = font.Font(size=16, weight="bold")
customTitleFont = font.Font(size=20, weight="bold")

# for hero text
Label(root, text="Stock Panda", bg="#8A908B", font=("Arial", 30, "bold"),fg="white").place(x=30, y=290)
Label(root, text="Some Description about the software", bg="#8A908B", font=("Arial", 20, "bold"),fg="white").place(x=30, y=340)


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
h1 = Label(container, text="Welcome Back", bg="#D9D9D9", font=customTitleFont)
h1.place(x=140, y=230)

# for text fields
phone = Entry(container,width=27,font=(10))
phone.place(x=90,y=300,height=38)

password = Entry(container,width=27,font=(10))
password.place(x=90,y=350,height=38)

confirmPassword = Entry(container,width=27,font=(10))
confirmPassword.place(x=90,y=400,height=38)

# for login button
login = Button(container, text="Log in", height=1, width=22, border=0, bg="#FF5252", fg="white",font=customButtonFont)
login.place(x=96,y=540)

# already have an account button
signUp = Button(container,text="Already have an account",border=0,fg="blue",bg="#D9D9D9",font=1)
signUp.place(x=145,y=650)


root.mainloop()