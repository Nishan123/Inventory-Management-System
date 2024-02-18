from tkinter import *
import sqlite3

def create_purchase_window(root):
    purchase=Toplevel(root)
    purchase.config(bg="#545454")
    purchase.title("Purchase Item")
    purchase.geometry("600x300")
    purchase.minsize(height=300,width=600)
    purchase.maxsize(height=300,width=600)
        
        
    conn = sqlite3.connect("inv.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS inventory(
          
          productID INTEGER PRIMARY KEY AUTOINCREMENT,
          product_name      TEXT,
          cp                TEXT,
          qty               TEXT,
          total             TEXT
          )""")
    conn.commit()
    conn.close()
    
    def onConfirmPurchase():
        conn = sqlite3.connect("inv.db")
        c=conn.execute("INSERT INTO inventory(product_name, cp, qty, total) VALUES(?,?,?,?)",(product_name_field.get(),costprice_field.get(),quantity_field.get(),totalPurchaseAmt))
        conn.commit()
        conn.close()
    
        
    # Purchase Label title
    title=Label(purchase,text="Purchase Item",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
        
    # for text field labels
    product_name_label=Label(purchase,text="Product Name",bg="#545454",fg="white",font=("Arial",10)).place(x=70,y=95)
    quantity_label = Label(purchase,text="Quantity",bg="#545454",fg="white",font=("Arial",10)).place(x=320,y=95)
    costprice_label = Label(purchase,text="Cost Price",bg="#545454",fg="white",font=("Arial",10)).place(x=427,y=95)
        
    # for text fields
    product_name_field=Entry(purchase,width=40)
    product_name_field.place(x=60,y=120,height=30)
        
    quantity_var = StringVar(value='')  # Set initial value to '0'
    quantity_field=Entry(purchase,width=15, textvariable=quantity_var)
    quantity_field.place(x=320,y=120,height=30)
        
    costprice_var = StringVar(value='')  # Set initial value to '0'
    costprice_field=Entry(purchase,width=18, textvariable=costprice_var)
    costprice_field.place(x=430,y=120,height=30)
        
    # for confirm button
    confirm_button=Button(purchase, text="Confirm Purchase", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"),command=onConfirmPurchase)
    confirm_button.place(x=210,y=230)
        
    # for total label
    total_purchase = Label(purchase,font=("Arial",16),bg="#545454",fg="white")
    total_purchase.place(x=420,y=234)


    def calculate_total(*args):
        global totalPurchaseAmt
        try:
            totalPurchaseAmt = int(costprice_var.get()) * int(quantity_var.get())
            total_purchase.config(text=f"Total: {totalPurchaseAmt}")
        except ValueError:
            total_purchase.config(text="Invalid input")
    
    quantity_var.trace_add("write", calculate_total)
    costprice_var.trace_add("write", calculate_total)
    purchase.mainloop() 


