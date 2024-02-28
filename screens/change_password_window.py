from tkinter import *
from tkinter import messagebox
import sqlite3


def check_and_update_passwd(prev_passwd, new_passwd):
    # Connect to the SQLite database
    conn = sqlite3.connect('inv.db')
    c = conn.cursor()

    # Fetch the id of the last row
    c.execute("SELECT id FROM userProfile ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]

    # Fetch the current password
    c.execute("SELECT passwd FROM userProfile WHERE id = ?", (last_id,))
    current_passwd = c.fetchone()[0]

    # Check if the previous password entered by the user matches the current password
    if prev_passwd == current_passwd:
        # Update the passwd and conf_passwd attributes in the last row
        c.execute("UPDATE userProfile SET passwd = ?, conf_passwd = ? WHERE id = ?", (new_passwd, new_passwd, last_id))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error", "Incorrect previous password")

def create_change_passwd_window(root, update_profile_screen_callback):
    change_passwd = Toplevel(root)
    change_passwd.config(bg="#545454")
    change_passwd.title("Change Password")
    change_passwd.geometry("600x300")
    change_passwd.minsize(height=300, width=600)
    change_passwd.maxsize(height=300, width=600)

    title = Label(change_passwd, text="Change Password", font=("Arial", 23), bg="#545454", fg="white").pack(pady=(15, 0))
    l1=Label(change_passwd,text="Enter old password -->").place(x=5,y=85)
    l2=Label(change_passwd,text="Enter new password -->").place(x=5,y=125)
    
    prev_passwd_field = Entry(change_passwd, width=60)
    prev_passwd_field.place(x=140, y=80, height=30)
    new_passwd_field = Entry(change_passwd, width=60)
    new_passwd_field.place(x=140, y=120, height=30)
    confirm_button = Button(change_passwd, text="Save Changes", height=2, width=22, border=0, bg="red", fg="white", font=("Arial", 10, "bold"), command=lambda: check_and_update_passwd(prev_passwd_field.get(), new_passwd_field.get()))
    confirm_button.place(x=210, y=230)
    change_passwd.mainloop()
