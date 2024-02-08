from tkinter import *
from tkinter import font
import os
import sqlite3

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)

def whenPurchaseItem():
    import purchase_window

def whenSaleItem():
    import sales_window

def whenHomeClicked():
    root.destroy()
    import home_screen
    
def onEnter(e):
    search_bar.delete(0, "end")

def onLeave(e):
    search = search_bar.get()
    if search == "":
        search_bar.insert(0, "Search")
        
        
        
# creating a icon path
icon_path = os.path.abspath("assets/stockpanda1.ico")

# using iconpath
root.iconbitmap(default=icon_path)

homeImg = PhotoImage(file="assets/home.png")
shoppingImg = PhotoImage(file="assets/shopping-cart.png")
dollarImg = PhotoImage(file="assets/dollar-sign.png")
userImg = PhotoImage(file="assets/user.png")
searchImg = PhotoImage(file="assets/search.png")
deleteImg = PhotoImage(file="assets/delete_icon.png")

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

# to add buttons to left
home_btn = Button(container, text="Home", image=homeImg, compound="left", height=35, width=260, bg="#FF5252",
                  fg="white", border=0, font=customButtonFont, command=whenHomeClicked )
home_btn.image = homeImg
home_btn.pack(pady=(280, 0))

purchase_btn = Button(container, text="Purchase", image=dollarImg, compound="left", height=35, width=260, bg="#FF5252",
                      fg="white", border=0, font=customButtonFont, command=whenPurchaseItem)
purchase_btn.image = dollarImg
purchase_btn.pack(pady=(10, 0))

saleBtn = Button(container, text="Sale", image=shoppingImg, compound="left", height=35, width=260, bg="#FF5252",
                 fg="white", border=0, font=customButtonFont, command=whenSaleItem )
saleBtn.image = shoppingImg
saleBtn.pack(pady=(10, 0))

account_btn = Button(container, text="Account", image=userImg, compound="left", height=35, width=260, bg="#FF5252",
                     fg="white", border=0, font=customButtonFont, )
account_btn.image = userImg
account_btn.pack(pady=(10, 0))

# to display app bar
appBar = Frame(root, height=60, width=800, bg="#7F7F7F")
appBar.pack_propagate(False)
appBar.pack()

# to display text logo
textlogo = PhotoImage(file="assets/textlogo.png")
logoDispaly = Label(appBar, image=textlogo, bg="#7F7F7F")
logoDispaly.place(x=30, y=10)

# search bar 
search_bar = Entry(appBar, width=22, font=7)
search_bar.insert(0, "Search")
search_bar.bind("<FocusIn>", onEnter)
search_bar.bind("<FocusOut>", onLeave)
search_bar.place(x=487, y=15, height=30)

search_btn = Button(appBar, image=searchImg, bg="#FF5252", )
search_btn.image = searchImg
search_btn.place(x=740, y=15)

# frame for profile page
stocks_frame=Frame(root,height=580,width=765,bg="#D9D9D9")
stocks_frame.pack_propagate(False)
stocks_frame.pack(padx=(6,0),pady=(30,0))

# frame to display profile details
profile_card = Frame(stocks_frame, height=560,width=330,bg="red")
profile_card.pack(side=RIGHT,padx=10)

# to display profile image


root.mainloop()