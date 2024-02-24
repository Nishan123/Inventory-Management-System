from tkinter import *
import sqlite3
from tkinter import messagebox

# Initialize total sales amount to 0
totalSalesAmt = 0


def update_home_screen(quantity_sold, cost_price):
    global totalSalesAmt
    totalSalesAmt -= quantity_sold * cost_price


def onConfirmSale(total_purchase):
    product_id = id_field.get()
    quantity_sold = int(quantity_field.get())

    conn = sqlite3.connect("inv.db")
    c = conn.cursor()

    c.execute("SELECT * FROM inventory WHERE productID=?", (product_id,))
    product_data = c.fetchone()
    if product_data:
        product_name = product_data[1]
        cost_price = int(product_data[2])
        available_quantity = int(product_data[3])
        old_total = int(product_data[4])

        if quantity_sold > available_quantity:
            messagebox.showerror("Error", "Insufficient quantity available!")
            conn.close()
            return

        total_sale_price = cost_price * quantity_sold
        new_db_toal = old_total-total_sale_price

        # Update quantity and total in the database
        updated_quantity = available_quantity - quantity_sold
        c.execute("UPDATE inventory SET qty=?, total=? WHERE productID=?",
                  (updated_quantity, new_db_toal, product_id))
        conn.commit()

        # Display total sale price on the sale window
        total_purchase.config(text=f"Total: {total_sale_price}")

        # Update total sale amount on the sale window
        global totalSalesAmt
        totalSalesAmt -= total_sale_price

        # Update total sale amount on the home screen
        update_home_screen(quantity_sold, cost_price)
        sale.destroy()

    else:
        messagebox.showerror("Error", "Product ID not found!")
    conn.close()


# Sale window
sale = Tk()
sale.config(bg="#545454")
sale.title("Sale Item")
sale.geometry("600x300")
sale.minsize(height=300, width=600)
sale.maxsize(height=300, width=600)

title = Label(sale, text="Sale Item", font=("Arial", 23),
              bg="#545454", fg="white").place(x=250, y=20)

id_label = Label(sale, text="ID", bg="#545454", fg="white",
                 font=("Arial", 10)).place(x=60, y=95)
product_name_label = Label(sale, text="Product Name", bg="#545454",
                           fg="white", font=("Arial", 10)).place(x=170, y=95)
quantity_label = Label(sale, text="Quantity", bg="#545454",
                       fg="white", font=("Arial", 10)).place(x=427, y=95)

id_field = Entry(sale, width=15)
id_field.place(x=60, y=120, height=30)

product_name_field = Entry(sale, width=40)
product_name_field.place(x=170, y=120, height=30)

quantity_field = Entry(sale, width=18)
quantity_field.place(x=430, y=120, height=30)

total_sale = Label(sale, text=f"Total: {totalSalesAmt}", font=(
    "Arial", 16), bg="#545454", fg="white")
total_sale.place(x=420, y=234)

confirm_button = Button(sale, text="Confirm Sale", height=2, width=22, border=0, bg="#004789", fg="white", font=("Arial", 10, "bold"),
                        command=lambda: onConfirmSale(total_sale))
confirm_button.place(x=210, y=230)

sale.mainloop()