from tkinter import *
from tkinter import font, filedialog
import os
import sqlite3

root = Tk()
root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)


def whenPurchaseItem():
    import purchase_window


def whenSaleItem():
    import sales_window


def whenHomeClicked():
    root.destroy()
    import home_screen


def onEnter(e):
    search_bar.delete(0, "end")


def onLeave(e):
    search = search_bar.get()
    if search == "":
        search_bar.insert(0, "Search")


# Function to handle the click event for profile picture
def on_profile_pic_click(event):
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    # Check if a file was selected
    if file_path:
        # Update profile image with the selected image
        profileimg.config(file=file_path)

        # Save file path to the database
        save_image_to_database(file_path)


# Function to save image file path to database
def save_image_to_database(file_path):
    # Connect to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE user SET profile_image = ? WHERE user_id = ?", (file_path,))  # create user_id, and user table in database to store these infos.

    # Commit changes and close connection
    conn.commit()
    conn.close()


# creating a icon path
icon_path = os.path.abspath("assets/stockpanda1.ico")

# using iconpath
root.iconbitmap(default=icon_path)

logoutImg = PhotoImage(file="assets/log-out.png")
homeImg = PhotoImage(file="assets/home.png")
shoppingImg = PhotoImage(file="assets/shopping-cart.png")
dollarImg = PhotoImage(file="assets/dollar-sign.png")
userImg = PhotoImage(file="assets/user.png")
searchImg = PhotoImage(file="assets/search.png")
deleteImg = PhotoImage(file="assets/delete_icon.png")
changeNameImg = PhotoImage(file="assets/change_name.png")
changePhoneImg = PhotoImage(file="assets/change_phone.png")
changePasswdImg = PhotoImage(file="assets/change_passwd.png")

# def back_img():
back_img = PhotoImage(file="assets/zoro.png")
back_img2 = PhotoImage(file="assets/zoro2.png")
colorimg = PhotoImage(file="assets/color.png")
colorimg2 = PhotoImage(file="assets/Rectangle54.png")

# Custom text styles
customButtonFont = font.Font(size=16, weight="bold")
customTitleFont = font.Font(size=20, weight="bold")

# container in left side
container = Frame(bg="#D9D9D9", height=700, width=300, )
container.pack_propagate(False)
container.pack(side=LEFT)

# to display image logo
imageLogo = PhotoImage(file="assets/imagelogo.png")
logoDispaly = Label(container, image=imageLogo, bg="#D9D9D9")
logoDispaly.place(x=65, y=30)

# to add buttons to left
home_btn = Button(container, text="Home", image=homeImg, compound="left", height=35, width=260, bg="#FF5252",
                  fg="white", border=0, font=customButtonFont, command=whenHomeClicked)
home_btn.image = homeImg
home_btn.pack(pady=(280, 0))

purchase_btn = Button(container, text="Purchase", image=dollarImg, compound="left", height=35, width=260, bg="#FF5252",
                      fg="white", border=0, font=customButtonFont, command=whenPurchaseItem)
purchase_btn.image = dollarImg
purchase_btn.pack(pady=(10, 0))

saleBtn = Button(container, text="Sale", image=shoppingImg, compound="left", height=35, width=260, bg="#FF5252",
                 fg="white", border=0, font=customButtonFont, command=whenSaleItem)
saleBtn.image = shoppingImg
saleBtn.pack(pady=(10, 0))

account_btn = Button(container, text="Account", image=userImg, compound="left", height=35, width=260, bg="#FF5252",
                     fg="white", border=0, font=customButtonFont, )
account_btn.image = userImg
account_btn.pack(pady=(10, 0))

# to display app bar
appBar = Frame(root, height=60, width=800, bg="#7F7F7F")
appBar.pack_propagate(False)
appBar.pack()

# to display text logo
textlogo = PhotoImage(file="assets/textlogo.png")
logoDispaly = Label(appBar, image=textlogo, bg="#7F7F7F")
logoDispaly.place(x=30, y=10)

# search bar
search_bar = Entry(appBar, width=22, font=7)
search_bar.insert(0, "Search")
search_bar.bind("<FocusIn>", onEnter)
search_bar.bind("<FocusOut>", onLeave)
search_bar.place(x=487, y=15, height=30)

search_btn = Button(appBar, image=searchImg, bg="#FF5252", )
search_btn.image = searchImg
search_btn.place(x=740, y=15)

# frame for profile page
profile_frame = Frame(root, height=580, width=765, bg="#D9D9D9")
profile_frame.pack_propagate(False)
profile_frame.pack(padx=(6, 0), pady=(30, 0))

# frame to display profile details
profile_card = Frame(profile_frame, height=560, width=330, bg="white")
back_label = Label(profile_card, image=colorimg2)
back_label.place(x=0, y=0, relheight=1, relwidth=1)
profile_card.pack_propagate(False)
profile_card.pack(side=RIGHT, padx=10)

# to display profile image
profileimg = PhotoImage(file='assets/camera.png')
profile_pic_frame = Frame(profile_card, height=150, width=150, relief='ridge',)
profile_pic_label = Label(profile_pic_frame, image=profileimg, cursor='hand2')
profile_pic_label.place(x=0, y=0, relheight=1, relwidth=1)
profile_pic_frame.pack(pady=(10, 0))

# Bind the click event to the profile picture label
profile_pic_label.bind("<Button-1>", on_profile_pic_click)


# to display store name
store_name = Label(profile_card, text="Store name", font=(
    "Arial", 20, "bold"), bg='#d599bc', background='#d599bc')
store_name.pack(pady=(20, 0))

# frame to display phone number
phone_frame = Frame(profile_card)
phone_frame.pack(pady=(10, 0))
Label(phone_frame, text="Phone:", background='#d599bc').grid(row=0, column=0)
store_phone = Label(phone_frame, text="9812345678", background='#d599bc')
store_phone.grid(row=0, column=1)


# log out button
logout_btn = Button(profile_card, text="Log Out", image=logoutImg, compound="left",
                    height=35, width=230, bg="#FF5252", fg="white", border=0, font=customButtonFont)
logout_btn.image = logoutImg
logout_btn.pack(pady=(175, 0))



# change name button
change_name_btn = Button(profile_frame, text="Change Name", image=changeNameImg, compound="left", height=35, width=260, bg="#D9D9D9",
                  fg="blue", border=0, font=customButtonFont)
change_name_btn.image = changeNameImg
change_name_btn.pack(pady=(200,0))

# change password button
change_name_btn = Button(profile_frame, text="Change Password", image=changePasswdImg, compound="left", height=35, width=260, bg="#D9D9D9",
                  fg="blue", border=0, font=customButtonFont)
change_name_btn.image = changePasswdImg
change_name_btn.pack()

# change phone button
change_name_btn = Button(profile_frame, text="Change", image=changePhoneImg, compound="left", height=35, width=260, bg="#D9D9D9",
                  fg="blue", border=0, font=customButtonFont)
change_name_btn.image = changePhoneImg
change_name_btn.pack()

root.mainloop()
