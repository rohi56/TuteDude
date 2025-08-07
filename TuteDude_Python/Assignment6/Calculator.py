#Calculator
from tkinter import *

# GUI Interaction
window = Tk()
window.title("Calculator")
window.geometry("400x600")

# Adding input field
entry = Entry(window, width=60, borderwidth=5)
entry.place(x=0, y=0)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif math == "division":
        if int(second_number) != 0:
            entry.insert(0, f_num / int(second_number))
        else:
            entry.insert(0, "Error: Division by Zero")


def button_add():
    first_number = entry.get()
    global math
    math = "addition"
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global math
    math = "subtraction"
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global math
    math = "multiplication"
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)
    
def button_divide():
    first_number = entry.get()
    global math
    math = "division"
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)
    
# Creating buttons
button1 = Button(window, text="1", width=5, height=2, command=lambda: button_click(1))
button2 = Button(window, text="2", width=5, height=2, command=lambda: button_click(2))
button3 = Button(window, text="3", width=5, height=2, command=lambda: button_click(3))
button4 = Button(window, text="4", width=5, height=2, command=lambda: button_click(4))
button5 = Button(window, text="5", width=5, height=2, command=lambda: button_click(5))
button6 = Button(window, text="6", width=5, height=2, command=lambda: button_click(6))
button7 = Button(window, text="7", width=5, height=2, command=lambda: button_click(7))
button8 = Button(window, text="8", width=5, height=2, command=lambda: button_click(8))
button9 = Button(window, text="9", width=5, height=2, command=lambda: button_click(9))
button0 = Button(window, text="0", width=5, height=2, command=lambda: button_click(0))
button_add = Button(window, text="+", width=5, height=2, command=button_add)
button_subtract = Button(window, text="-", width=5, height=2, command=button_subtract)
button_multiply = Button(window, text="*", width=5, height=2, command=button_multiply)
button_divide = Button(window, text="/", width=5, height=2, command=button_divide)
button_equal = Button(window, text="=", width=5, height=2, command=button_equal)
button_clear = Button(window, text="C", width=5, height=2, command=button_clear)

button1.place(x=0, y=50)
button2.place(x=100, y=50)
button3.place(x=200, y=50)
button4.place(x=0, y=150)
button5.place(x=100, y=150)
button6.place(x=200, y=150)
button7.place(x=0, y=250)
button8.place(x=100, y=250)
button9.place(x=200, y=250)
button0.place(x=100, y=350)
button_add.place(x=300, y=50)
button_subtract.place(x=300, y=150)
button_multiply.place(x=300, y=250)
button_divide.place(x=300, y=350)
button_equal.place(x=200, y=350)
button_clear.place(x=0, y=350)


#main loop to run the application
mainloop()