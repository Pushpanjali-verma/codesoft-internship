from tkinter import *


window = Tk()
window.title("Simple Calculator")


entry_field = Entry(window, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: click_button(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: click_button(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: click_button(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: click_button(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: click_button(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: click_button(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: click_button(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: click_button(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: click_button(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: click_button(0))


button_add = Button(window, text="+", padx=40, pady=20, command=lambda: click_button("+"))
button_subtract = Button(window, text="-", padx=40, pady=20, command=lambda: click_button("-"))
button_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: click_button("*"))
button_divide = Button(window, text="/", padx=40, pady=20, command=lambda: click_button("/"))
button_equals = Button(window, text="=", padx=40, pady=20, command=lambda: click_button("="))
button_clear = Button(window, text="Clear", padx=80, pady=20, command=lambda: click_button("Clear"))


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equals.grid(row=4, column=2, columnspan=2)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_clear.grid(row=6, column=0, columnspan=3)


def click_button(number):
    current = entry_field.get()
    if number == "Clear":
        entry_field.delete(0, END)
    elif number == "=":
        try:
            result = eval(current)
            entry_field.delete(0, END)
            entry_field.insert(0, result)
        except Exception as e:
            entry_field.delete(0, END)
            entry_field.insert(0, "Error")
    else:
        entry_field.insert(END, number)

# start the GUI event loop
window.mainloop()