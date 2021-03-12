#===========FURRO404===========#
import tkinter as tk
from tkinter import *
#---------------------------#
root = Tk()
root.title("Calculator")
e = Entry(root, width = 40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#----------------------------------------------------------------------#
def smile():
    exit()

def butt_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def butt_clear():
    e.delete(0, END)

def butt_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
        
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
        
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
        
    elif math == "division":
        div = round((f_num) / int(second_number))
        e.insert(0, div)
                
def butt_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def butt_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def butt_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    
def butt_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
#--------------------------------#
#Define buttons
butt1 = Button(root, text="1", padx=40, pady=20, command=lambda: butt_click(1))
butt2 = Button(root, text="2", padx=40, pady=20, command=lambda: butt_click(2))
butt3 = Button(root, text="3", padx=40, pady=20, command=lambda: butt_click(3))
butt4 = Button(root, text="4", padx=40, pady=20, command=lambda: butt_click(4))
butt5 = Button(root, text="5", padx=40, pady=20, command=lambda: butt_click(5))
butt6 = Button(root, text="6", padx=40, pady=20, command=lambda: butt_click(6))
butt7 = Button(root, text="7", padx=40, pady=20, command=lambda: butt_click(7))
butt8 = Button(root, text="8", padx=40, pady=20, command=lambda: butt_click(8))
butt9 = Button(root, text="9", padx=40, pady=20, command=lambda: butt_click(9))
butt0 = Button(root, text="0", padx=40, pady=20, command=lambda: butt_click(0))
butt = Button(root, text=":)", padx=40, pady=20, command=smile)
butt_equal = Button(root, text="=", padx=90, pady=20, command=butt_equal)
butt_clear = Button(root, text="Clear", padx=80, pady=20, command=butt_clear)
butt_add = Button(root, text="+", padx=39, pady=20, command=butt_add)
butt_sub = Button(root, text="-", padx=40, pady=20, command=butt_sub)
butt_mult = Button(root, text="*", padx=41, pady=20, command=butt_mult)
butt_div = Button(root, text="/", padx=41, pady=20, command=butt_div)

#Put buttons on screen
butt1.grid(row=3,column=0)
butt2.grid(row=3,column=1)
butt3.grid(row=3,column=2)
butt4.grid(row=2,column=0)
butt5.grid(row=2,column=1)
butt6.grid(row=2,column=2)
butt7.grid(row=1,column=0)
butt8.grid(row=1,column=1)
butt9.grid(row=1,column=2)
butt0.grid(row=4,column=0)
butt.grid(row=5, column=4)

butt_equal.grid(row=4, column=1, columnspan=2)
butt_clear.grid(row=5, column=1, columnspan=2)
butt_add.grid(row=4, column = 4)
butt_sub.grid(row=3, column = 4)
butt_mult.grid(row=2, column = 4)
butt_div.grid(row=1, column = 4)

root.mainloop()
#===========FURRO404===========#
