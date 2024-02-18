# stock items list tile frame
itemFrame= Frame(scroll_frame,bg="red",height=34,width=750)
itemFrame.pack_propagate(False)
itemFrame.pack(pady=10)

delete_btn = Button(itemFrame, image=deleteImg )
delete_btn.image = deleteImg
delete_btn.place(x=1,y=2,)

item_id = Label(itemFrame,text="1",width=6,font=10,anchor="w")
item_id.place(x=39,y=2,height=30)

item_name = Label(itemFrame,text="Shampoo",width=25,font=10,anchor="w")
item_name.place(x=116,y=2,height=30)

item_qty_field = Label(itemFrame,text="20",width=9,font=10,anchor="w")
item_qty_field.place(x=401,y=2,height=30)

item_cp_field = Label(itemFrame,text="30",width=9,font=10,anchor="w")
item_cp_field.place(x=510,y=2,height=30)

item_total_field = Label(itemFrame,text="600",width=11,font=10,anchor="w")
item_total_field.place(x=620,y=2,height=30)