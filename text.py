from tkinter import Tk, Frame, Label, PhotoImage

root = Tk()

# Load the image file
img = PhotoImage(file="assets/home.png")

# Create a frame as a custom button
frame = Frame(root, bd=1, relief='raised')

# Create a label for the image
img_label = Label(frame, image=img)
img_label.pack(side='left')

# Create a label for the text
text_label = Label(frame, text="Your Text")
text_label.pack(side='left')

# Keep a reference to the image to prevent it from being garbage collected
img_label.image = img

frame.pack()

root.mainloop()
