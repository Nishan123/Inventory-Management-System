from tkinter import *
from tkinter import font

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)


homeImg = PhotoImage(file="assets/home.png")
shoppingImg = PhotoImage(file="assets/shopping-cart.png")
dollarImg = PhotoImage(file="assets/dollar-sign.png")
userImg = PhotoImage(file="assets/user.png")




# Custom text styles
customButtonFont = font.Font(size=16, weight="bold")
customTitleFont = font.Font(size=20, weight="bold")

# container in left side
container = Frame(bg="#D9D9D9", height=700, width=300)
container.pack_propagate(False)
container.pack(side=LEFT)

# to display image logo
imageLogo = PhotoImage(file="assets/imagelogo.png")
logoDispaly = Label(container, image=imageLogo, bg="#D9D9D9")
logoDispaly.place(x=65, y=30)

# to display app bar
appBar = Frame(root, height=60, width=800, bg="#7F7F7F")
appBar.pack()

# to display text logo
textlogo = PhotoImage(file="assets/textlogo.png", )
logoDispaly = Label(appBar, image=textlogo, bg="#7F7F7F")
logoDispaly.place(x=30, y=10)

# to add buttons to left

home_btn = Button(container, text="Home", image=homeImg, compound="left",height=35,width=260,bg="#FF5252",fg="white",border=0,font=customButtonFont,)
home_btn.image = homeImg
home_btn.pack(pady=(280,0))

purchase_btn = Button(container, text="Purchase", image=dollarImg, compound="left",height=35,width=260,bg="#FF5252",fg="white",border=0,font=customButtonFont,)
purchase_btn.image = dollarImg
purchase_btn.pack(pady=(10,0))

saleBtn = Button(container, text="Sale", image=shoppingImg, compound="left",height=35,width=260,bg="#FF5252",fg="white",border=0,font=customButtonFont,)
saleBtn.image = shoppingImg
saleBtn.pack(pady=(10,0))

account_btn = Button(container, text="Account", image=userImg, compound="left",height=35,width=260,bg="#FF5252",fg="white",border=0,font=customButtonFont,)
account_btn.image = userImg
account_btn.pack(pady=(10,0))

root.mainloop()
