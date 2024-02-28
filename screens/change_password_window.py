from tkinter import *
import sqlite3

def update_phone(new_passwd):
    # Connect to the SQLite database
    conn = sqlite3.connect('inv.db')
    c = conn.cursor()

    # Fetch the id of the last row
    c.execute("SELECT id FROM userProfile ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]

    # Update the str_name attribute value in the last row
    c.execute("UPDATE userProfile SET passwd = ? WHERE id = ?", (new_passwd, last_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def create_change_passwd_window(root,update_profile_screen_callback):
    change_passwd=Toplevel(root)
    change_passwd.config(bg="#545454")
    change_passwd.title("Change Passwd")
    change_passwd.geometry("600x300")
    change_passwd.minsize(height=300,width=600)
    change_passwd.maxsize(height=300,width=600)
        
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
  
    title=Label(change_passwd,text="Change Password",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
    
    new_passwd_field=Entry(change_passwd,width=60)
    new_passwd_field.place(x=130,y=120,height=30)

    confirm_button=Button(change_passwd, text="Save Changes", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"), command= lambda:update_phone(new_passwd_field.get()))
    confirm_button.place(x=210,y=230)
        


    change_passwd.mainloop() 
    