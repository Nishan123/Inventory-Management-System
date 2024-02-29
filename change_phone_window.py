from tkinter import *
import sqlite3
from tkinter import messagebox
def update_str_phone(new_phone, store_phone):
    if len(new_phone)==10:
        # Connect to the SQLite database
        conn = sqlite3.connect('inv.db')
        c = conn.cursor()
        # Fetch the id of the last row
        c.execute("SELECT id FROM userProfile ORDER BY id DESC LIMIT 1")
        last_id = c.fetchone()[0]
        # Update the str_phone attribute value in the last row
        c.execute("UPDATE userProfile SET user_phone = ? WHERE id = ?", (new_phone, last_id))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Update the store_phone label
        store_phone.config(text=new_phone)
    else:
        messagebox.showerror(title="Profile Status",message="Length of phone number must be 10 digit")

def create_change_phone_window(root, update_profile_screen_callback_phone, store_phone):
    change_phone=Toplevel(root)
    change_phone.config(bg="#545454")
    change_phone.title("Purchase Item")
    change_phone.geometry("600x300")
    change_phone.minsize(height=300,width=600)
    change_phone.maxsize(height=300,width=600)

    title=Label(change_phone,text="Change phone",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
        
    new_phone_field=Entry(change_phone,width=60)
    new_phone_field.place(x=125,y=120,height=30)
        
    confirm_button=Button(change_phone, text="Save Changes", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"), command=lambda: update_str_phone(new_phone_field.get(), store_phone))
    confirm_button.place(x=210,y=230)
        
    change_phone.mainloop()

    