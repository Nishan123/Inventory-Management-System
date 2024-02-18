
from tkinter import *
from tkinter import font
import purchase_window
import sqlite3

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)

def whenPurchaseItem():
    purchase_window.create_purchase_window(root)
    
def whenAccountPressed():
    root.destroy()
    import profile_screen

def whenSaleItem():
    import sales_window
def onEnter(e):
    search_bar.delete(0, "end")

def onLeave(e):
    search = search_bar.get()
    if search == "":
        search_bar.insert(0, "Search")
        

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

search_btn = Button(appBar, image=searchImg, bg="#FF5252")
search_btn.image = searchImg
search_btn.place(x=740, y=15)

# to add buttons to left
home_btn = Button(container, text="Home", image=homeImg, compound="left", height=35, width=260, bg="#FF5252",
                  fg="white", border=0, font=customButtonFont, )
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
                     fg="white", border=0, font=customButtonFont,command=whenAccountPressed )
account_btn.image = userImg
account_btn.pack(pady=(10, 0))

# for avialable stocks label
Label(root,text="Availabe Stocks",font=("Arial",18,"bold"),bg="#8A908B").place(x=320,y=95)

# for toal purchase, sales and stocks value
valueContainer= Frame(root)
valueContainer.place(x=874,y=100)

stocksValue = Label(valueContainer,text="Stocks:XXX")
stocksValue.grid(row=0,column=0)

purchaseValue = Label(valueContainer,text="Purchase:XXX")
purchaseValue.grid(row=0,column=1)

saleValue = Label(valueContainer,text="Sales:XXX")
saleValue.grid(row=0,column=2)

# frame to store list of avaialble stocks
stocks_frame=Frame(root,height=520,width=790,bg="#D9D9D9")
stocks_frame.pack_propagate(False)
stocks_frame.pack(padx=(4,0),pady=(70,0))

# frame to store labels
stocks_frame_labels=Frame(stocks_frame,height=520,width=760,bg="#D9D9D9")
stocks_frame_labels.place(x=50,y=10)



# labels inside stocks container
id_label = Label(stocks_frame_labels,text="ID",font=("Arial",13,"bold",),bg="#D9D9D9").grid(row=0,column=0,padx=(0,52))
productName_label = Label(stocks_frame_labels,text="Product Name",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=1,padx=(0,168))
qty_label=Label(stocks_frame_labels,text="Qty",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=2,padx=(0,70))
cp_label=Label(stocks_frame_labels,text="CP",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=3,padx=(0,76))
total_label=Label(stocks_frame_labels,text="Total",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=4,padx=(0,0))


# for scroll frame
scroll_frame=Frame(stocks_frame,bg="pink",height=480,width=775,)
scroll_frame.pack_propagate(False)
scroll_frame.pack(side=BOTTOM)

# to display scroll bar
yscroll = Scrollbar(scroll_frame)
yscroll.pack(side=RIGHT, fill=Y)

conn = sqlite3.connect("inv.db")
c=conn.cursor()
c.execute("SELECT * FROM inventory")
stocks = c.fetchall()
all_stocks = ""
for stock in stocks:
    all_stocks+=str(stock[0])+str(stock[1])+str(stock[2])+str(stock[3])+str(stock[4])
    itemFrame= Frame(scroll_frame,bg="red",height=34,width=750)
    itemFrame.pack_propagate(False)
    itemFrame.pack(pady=(10,0))

    delete_btn = Button(itemFrame, image=deleteImg )
    delete_btn.image = deleteImg
    delete_btn.place(x=1,y=2,)

    item_id = Label(itemFrame,text=stock[0],width=6,font=10,anchor="w")
    item_id.place(x=39,y=2,height=30)

    item_name = Label(itemFrame,text=stock[1],width=25,font=10,anchor="w")
    item_name.place(x=116,y=2,height=30)

    item_qty_field = Label(itemFrame,text=stock[2],width=9,font=10,anchor="w")
    item_qty_field.place(x=401,y=2,height=30)

    item_cp_field = Label(itemFrame,text=stock[3],width=9,font=10,anchor="w")
    item_cp_field.place(x=510,y=2,height=30)

    item_total_field = Label(itemFrame,text=stock[4],width=11,font=10,anchor="w")
    item_total_field.place(x=620,y=2,height=30)
    
    
    

root.mainloop()
