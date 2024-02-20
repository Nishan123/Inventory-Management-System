from tkinter import *
import sqlite3



def create_change_name_window(root,update_profile_screen_callback):
    change_name=Toplevel(root)
    change_name.config(bg="#545454")
    change_name.title("Purchase Item")
    change_name.geometry("600x300")
    change_name.minsize(height=300,width=600)
    change_name.maxsize(height=300,width=600)
        
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

        
        
  
    title=Label(change_name,text="Change Name",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
        
    
    new_name_field=Entry(change_name,width=60)
    new_name_field.place(x=130,y=120,height=30)
        

        

    confirm_button=Button(change_name, text="Save Changes", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"))
    
    confirm_button.place(x=210,y=230)
        


    change_name.mainloop() 
    
