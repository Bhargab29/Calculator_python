import cmath
import math
from tkinter import *
from turtle import bgcolor

window = Tk()
window.title("Calculator")
window['bg']="green"

e = Entry(window, width=30, borderwidth=3)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	#math
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))
	
	if math == "squared":
		e.insert(0, f_num * f_num)

	if math == "cubed":
		e.insert(0, f_num * f_num * f_num)

	if math == "to_the_power_of":
		e.insert(0, f_num ** int(second_number))

	if math == "square_root":
		e.insert(0, f_num ** 0.5)

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)




# Def buttons

button_1 = Button(window, text="1", padx=20, pady=10, bg="gray75", command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=20, pady=10, bg="gray75", command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=20, pady=10, bg="gray75", command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=20, pady=10, bg="gray75", command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=20, pady=10, bg="gray75", command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=20, pady=10, bg="gray75", command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=20, pady=10, bg="gray75", command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=20, pady=10, bg="gray75", command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=20, pady=10, bg="gray75", command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=20, pady=10, bg="gray75", command=lambda: button_click(0))
button_add = Button(window, text="+", padx=19, pady=10, bg="sky blue", command=button_add)
button_equal = Button(window, text="=", padx=19, pady=10, bg="yellow", command=button_equal)
button_clear = Button(window, text="Clear", padx=9, pady=10, bg="dark red", command=button_clear)

button_subtract = Button(window, text="-", padx=21, pady=10, bg="sky blue", command=button_subtract)
button_multiply = Button(window, text="*", padx=21, pady=10, bg="sky blue", command=button_multiply)
button_divide = Button(window, text="/", padx=21, pady=10, bg="sky blue", command=button_divide)


 # put buttons on screen

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_add.grid(row=1, column=0)
button_equal.grid(row=4, column=3)

button_subtract.grid(row=2, column=0)
button_multiply.grid(row=3, column=0)
button_divide.grid(row=4, column=0)



window.mainloop()
