from tkinter import *
sale=Tk()
sale.config(bg="#545454")
sale.title("Sale Item")
sale.geometry("600x300")
sale.minsize(height=300,width=600)
sale.maxsize(height=300,width=600)


    
# Purchase Label title
title=Label(sale,text="Sale Item",font=("Arial",23),bg="#545454",fg="white").place(x=250,y=20)
    

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
sale.mainloop()