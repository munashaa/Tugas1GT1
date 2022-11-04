from tkinter import *
window = Tk()
window.title("kasir GUI di Python")
window.minsize(width=500, height=700)
window.configure(bg="green")

def button_clicked ():
    Americano_total = int(lbl_sb.get())*20
    Mocha_Latte_total = int(lbl2_sb.get())*15
    Cappuccino_total = int(lbl3_sb.get())*17
    Ice_Tea_total = int(lbl4_sb.get())*8
    Mineral_Water_total = int(lbl5_sb.get())*5
    total_bills = Americano_total + Mocha_Latte_total + Cappuccino_total + Ice_Tea_total + Mineral_Water_total
    bills = Label(text=f"Total pesanan {total_bills}k",font=("Times New Roman",15,"bold"),bg="green")
    bills.place(x=20,y=250)

title_name = Label(text="Hits Cafe",font=("Times New Roman",20,"bold"),bg="green")
title_name.grid(column=1,row=0)

title_name2 = Label(text="List Menu:",font=("Times New Roman",15,"bold"),bg="green")
title_name2.grid(column=0,row=1)

lbl = Label(text="Americano (20k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl.place(x=10, y=70)
lbl_sb = Spinbox(from_=0, to=10, width=5)
lbl_sb.place(x=200, y=75)
 
lbl2 = Label(text="Mocha Latte (15k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl2.place(x=10, y=95)
lbl2_sb= Spinbox(from_=0, to=10, width=5)
lbl2_sb.place(x=200, y=100)
 
lbl3 = Label(text="Cappuccino (17k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl3.place(x=10, y=120)
lbl3_sb = Spinbox(from_=0, to=10, width=5)
lbl3_sb.place(x=200, y=125)

lbl4 = Label(text="Ice Tea (8k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl4.place(x=10, y=145)
lbl4_sb = Spinbox(from_=0, to=10, width=5)
lbl4_sb.place(x=200, y=150)

lbl5 = Label(text="Mineral Water (5k)\t: ",anchor="e",font=("Times New Roman",15,"normal"),bg="green")
lbl5.place(x=10, y=170)
lbl5_sb = Spinbox(from_=0, to=10, width=5)
lbl5_sb.place(x=200, y=175)

finish = Button(text="order", command=button_clicked)
finish.place(x=20 , y=200)

window.mainloop()