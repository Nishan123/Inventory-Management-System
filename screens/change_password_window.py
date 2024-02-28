from tkinter import *
import sqlite3
from profile_screen import update_gui

def update_password(new_password):
     # Connect to the SQLite database
    conn = sqlite3.connect('inv.db')
    c = conn.cursor()

    # Fetch the id of the last row
    c.execute("SELECT id FROM userProfile ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]

    # Update the str_name attribute value in the last row
    c.execute("UPDATE userProfile SET user_phone = ? WHERE id = ?", (new_password, last_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Update the GUI
    update_gui()
    

def create_change_password_window(root,update_profile_screen_callback):
    change_password=Toplevel(root)
    change_password.config(bg="#545454")
    change_password.title("Change Phone")
    change_password.geometry("600x300")
    change_password.minsize(height=300,width=600)
    change_password.maxsize(height=300,width=600)
        
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
  
    title=Label(change_password,text="Enter old password",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
        
    
    old_pass_field=Entry(change_password,width=60)
    old_pass_field.place(x=125,y=120,height=30)

    confirm_button=Button(change_password, text="Continue", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"), command= lambda:update_password(old_pass_field.get()))
    confirm_button.place(x=210,y=230)
        


    change_password.mainloop() 