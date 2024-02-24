from tkinter import *
import sqlite3
from tkinter import messagebox

totalSalesAmt = 0  # Initialize totalSalesAmt with an initial value


def update_inventory(product_id, sale_quantity):
    conn = sqlite3.connect("inv.db")
    c = conn.cursor()

    # Retrieve product details from the database
    c.execute("SELECT * FROM inventory WHERE productID=?", (product_id,))
    product = c.fetchone()

    if product:
        # Calculate updated quantity after sale
        remaining_quantity = int(product[3]) - int(sale_quantity)
        if remaining_quantity >= 0:
            # Update the quantity in the database
            c.execute("UPDATE inventory SET qty=? WHERE productID=?",
                      (remaining_quantity, product_id))
            conn.commit()

            # Calculate individual price and update total price
            individual_price = float(product[2]) * int(sale_quantity)
            total_price = float(product[4]) - individual_price
            c.execute("UPDATE inventory SET total=? WHERE productID=?",
                      (total_price, product_id))
            conn.commit()
        else:
            print("Sale quantity exceeds available quantity.")
    else:
        print("Product not found in inventory.")

    conn.close()


# Create the sales window
sale = Tk()
sale.config(bg="#545454")
sale.title("Sale Item")
sale.geometry("600x300")
sale.minsize(height=300, width=600)
sale.maxsize(height=300, width=600)


def confirm_sale():
    product_id = id_field.get()
    sale_quantity = quantity_field.get()

    if product_id and sale_quantity:
        update_inventory(product_id, sale_quantity)
    else:
        print("Please enter product ID and sale quantity.")
        sale.destroy()


# Sale Label title
title = Label(sale, text="Sale Item", font=(
    "Arial", 23), bg="#545454", fg="white")
title.place(x=250, y=20)

# Text field labels
id_label = Label(sale, text="ID", bg="#545454", fg="white", font=("Arial", 10))
id_label.place(x=60, y=95)
product_name_label = Label(sale, text="Product Name",
                           bg="#545454", fg="white", font=("Arial", 10))
product_name_label.place(x=170, y=95)
quantity_label = Label(sale, text="Quantity", bg="#545454",
                       fg="white", font=("Arial", 10))
quantity_label.place(x=427, y=95)

# Text fields
id_field = Entry(sale, width=15)
id_field.place(x=60, y=120, height=30)
product_name_field = Entry(sale, width=40)
product_name_field.place(x=170, y=120, height=30)
quantity_field = Entry(sale, width=18)
quantity_field.place(x=430, y=120, height=30)

# Confirm button
confirm_button = Button(sale, text="Confirm Sale", height=2, width=22, border=0, bg="#004789", fg="white",
                        font=("Arial", 10, "bold"), command=confirm_sale)
confirm_button.place(x=210, y=230)

# Total label
total_purchase = Label(sale, text=f"Total: {totalSalesAmt}", font=(
    "Arial", 16), bg="#545454", fg="white")
total_purchase.place(x=450, y=234)

sale.mainloop()
