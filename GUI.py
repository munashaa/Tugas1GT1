from tkinter import *
window = Tk()
window.title("kasir GUI di Python")
window.minsize(width=500, height=700)
window.configure(bg="green")

title_name = Label(text="Hits Cafe",font=("Times New Roman",20,"bold"),bg="green")
title_name.grid(column=1,row=0)

title_name2 = Label(text="List Menu:",font=("Times New Roman",15,"bold"),bg="green")
title_name2.grid(column=0,row=1)

lbl = Label(text="Americano (20k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl.place(x=10, y=70)
lbl = Spinbox(from_=0, to=10, width=5)
lbl.place(x=200, y=75)
 
lbl2 = Label(text="Mocha Latte (15k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl2.place(x=10, y=95)
lbl2 = Spinbox(from_=0, to=10, width=5)
lbl2.place(x=200, y=100)
 
lbl3 = Label(text="Cappuccino (17k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl3.place(x=10, y=120)
lbl3 = Spinbox(from_=0, to=10, width=5)
lbl3.place(x=200, y=125)

lbl4 = Label(text="Ice Tea (8k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl4.place(x=10, y=145)
lbl4 = Spinbox(from_=0, to=10, width=5)
lbl4.place(x=200, y=150)

lbl2 = Label(text="Mineral Water (5k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl2.place(x=10, y=170)
lbl2 = Spinbox(from_=0, to=10, width=5)
lbl2.place(x=200, y=175)

window.mainloop()