from tkinter import *
from tkinter import font

root = Tk()


def login():
    root.destroy()
    from screens import login_screen


def signup():
    root.destroy()
    from screens import signup_screen


root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)

container = Frame(bg="#D9D9D9", height=700, width=450)
container.pack_propagate(False)
container.pack(side=RIGHT)

# Custom text styles
customButtonFont = font.Font(size=10, weight="bold")
customTitleFont = font.Font(size=20, weight="bold")

# to display text logo
textlogo = PhotoImage(file="assets/textlogo.png")
logoDispaly = Label(root, image=textlogo, bg="#8A908B")
logoDispaly.place(x=30, y=20)

# for hero text
Label(root, text="Stock Panda", bg="#8A908B", font=("Arial", 30, "bold"), fg="white").place(x=30, y=290)
Label(root, text="Some Description about the software", bg="#8A908B", font=("Arial", 20, "bold"), fg="white").place(
    x=30, y=340)

# Get started text
h1 = Label(container, text="Get Started", bg="#D9D9D9", font=customTitleFont)
h1.place(x=150, y=260)

# to place button horizantally
buttonContainer = Frame(container, height=5, width=400, bg="#D9D9D9")
buttonContainer.place(x=60, y=320)

login = Button(buttonContainer, text="Log in", height=2, width=20, border=0, bg="#FF5252", fg="white",
               font=customButtonFont, command=login)
login.grid(column=0, row=0)

signup = Button(buttonContainer, text="Sign up", height=2, width=20, border=0, bg="#FF5252", fg="white",
                font=customButtonFont, command=signup)
signup.grid(column=1, row=0, padx=15)

root.mainloop()
