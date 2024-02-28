import sqlite3
from tkinter import *


def update_str_name(new_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('inv.db')
    c = conn.cursor()

    # Fetch the id of the last row
    c.execute("SELECT id FROM userProfile ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]

    # Update the str_name attribute value in the last row
    c.execute("UPDATE userProfile SET str_name = ? WHERE id = ?", (new_name, last_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()



def create_change_name_window(root,update_profile_screen_callback_name):
    change_name=Toplevel(root)
    change_name.config(bg="#545454")
    change_name.title("Purchase Item")
    change_name.geometry("600x300")
    change_name.minsize(height=300,width=600)
    change_name.maxsize(height=300,width=600)

    title=Label(change_name,text="Change Name",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
        
    new_name_field=Entry(change_name,width=60)
    new_name_field.place(x=125,y=120,height=30)
        
    confirm_button=Button(change_name, text="Save Changes", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"), command=lambda: update_str_name(new_name_field.get()))
    confirm_button.place(x=210,y=230)
        
    change_name.mainloop()

