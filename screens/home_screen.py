from tkinter import *
from tkinter import font
from tkinter import Tk, Label, Entry, Button, StringVar

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)

# Make quantity_var and costprice_var global variables
quantity_var = StringVar(value='0')  # Set initial value to '0'
costprice_var = StringVar(value='0')  # Set initial value to '0'

def whenPurchaseItem():
    purchase=Tk()
    purchase.config(bg="#545454")
    purchase.title("Purchase Item")
    purchase.geometry("600x300")
    purchase.minsize(height=300,width=600)
    purchase.maxsize(height=300,width=600)
    
    # Purchase Label title
    title=Label(purchase,text="Purchase Item",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
    
    # for text field labels
    product_name_label=Label(purchase,text="Product Name",bg="#545454",fg="white",font=("Arial",10)).place(x=70,y=95)
    quantity_label = Label(purchase,text="Quantity",bg="#545454",fg="white",font=("Arial",10)).place(x=320,y=95)
    costprice_label = Label(purchase,text="Cost Price",bg="#545454",fg="white",font=("Arial",10)).place(x=427,y=95)
    
    # for text fields
    product_name_field=Entry(purchase,width=40)
    product_name_field.place(x=60,y=120,height=30)
    
    quantity_var = StringVar(value='0')  # Set initial value to '0'
    quantity_field=Entry(purchase,width=15, textvariable=quantity_var)
    quantity_field.place(x=320,y=120,height=30)
    
    costprice_var = StringVar(value='0')  # Set initial value to '0'
    costprice_field=Entry(purchase,width=18, textvariable=costprice_var)
    costprice_field.place(x=430,y=120,height=30)
    
    # for confirm button
    confirm_button=Button(purchase, text="Confirm Purchase", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"))
    confirm_button.place(x=210,y=230)
    
    # for total label
    total_purchase = Label(purchase,font=("Arial",16),bg="#545454",fg="white")
    total_purchase.place(x=450,y=234)

    def calculate_total(*args):
        try:
            totalPurchaseAmt = int(costprice_var.get()) * int(quantity_var.get())
            total_purchase.config(text=f"Total: {totalPurchaseAmt}")
        except ValueError:
            total_purchase.config(text="Invalid input")

    quantity_var.trace_add("write", calculate_total)
    costprice_var.trace_add("write", calculate_total)
    purchase.mainloop()

def whenSaleItem():
    sale=Tk()
    sale.config(bg="#545454")
    sale.title("Sale Item")
    sale.geometry("600x300")
    sale.minsize(height=300,width=600)
    sale.maxsize(height=300,width=600)
    
    # Purchase Label title
    title=Label(sale,text="Sale Item",font=("Arial",23),bg="#545454",fg="white").place(x=50,y=20)
    
    # for search bar     
    sale_search_bar = Entry(sale, width=22, font=7)
    sale_search_bar.insert(0,"Search")
    sale_search_bar.bind("<FocusOut>", onLeave)
    sale_search_bar.bind("<FocusIn>", onEnter)
    sale_search_bar.place(x=300, y=20, height=30)
    
    # for text field labels
    id_label=Label(sale,text="ID",bg="#545454",fg="white",font=("Arial",10)).place(x=60,y=95)
    product_name_label = Label(sale,text="Product Name",bg="#545454",fg="white",font=("Arial",10)).place(x=170,y=95)
    quantity_label = Label(sale,text="Quantity",bg="#545454",fg="white",font=("Arial",10)).place(x=427,y=95)
    
    # for text fields
    id_field=Entry(sale,width=15)
    id_field.place(x=60,y=120,height=30)
    
    product_name_field=Entry(sale,width=40)
    product_name_field.place(x=170,y=120,height=30)
    
    quantity_field=Entry(sale,width=18)
    quantity_field.place(x=430,y=120,height=30)
    
    
    # for confirm button
    confirm_button=Button(sale, text="Confirm Sale", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"))
    confirm_button.place(x=210,y=230)
    
    # variable to calculate total price
    totalSalesAmt= "XXX"
    
    # for total label
    total_purchase = Label(sale,text=f"Total:{totalSalesAmt}",font=("Arial",16),bg="#545454",fg="white")
    total_purchase.place(x=450,y=234)
    
    
    
    
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
search_bar.place(x=480, y=15, height=30)

search_btn = Button(appBar, image=searchImg, bg="#FF5252", )
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
                     fg="white", border=0, font=customButtonFont, )
account_btn.image = userImg
account_btn.pack(pady=(10, 0))

# for avialbel stocks label
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
stocks_frame=Frame(root,height=520,width=765,bg="#D9D9D9")
stocks_frame.pack_propagate(False)
stocks_frame.pack(padx=(6,0),pady=(70,0))

# frame to store labels
stocks_frame_labels=Frame(stocks_frame,height=520,width=760,bg="#D9D9D9")
stocks_frame_labels.place(x=50,y=10)

# labels inside stocks container
id_label = Label(stocks_frame_labels,text="ID",font=("Arial",13,"bold",),bg="#D9D9D9").grid(row=0,column=0,padx=(0,70))
productName_label = Label(stocks_frame_labels,text="Product Name",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=1,padx=(0,170))
qty_label=Label(stocks_frame_labels,text="Qty",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=2,padx=(0,80))
cp_label=Label(stocks_frame_labels,text="CP",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=3,padx=(0,60))
total_label=Label(stocks_frame_labels,text="Total",font=("Arial",13,"bold"),bg="#D9D9D9").grid(row=0,column=4,padx=(0,0))





root.mainloop()
