from tkinter import *
from tkinter import messagebox
from random import choice,  shuffle
def generate_password():
    length = entry1.get()
    complex= entry2.get()
    if len(length) == 0 or len(complex) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
        letters_numbers= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        letters_numbers_symbol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   '!', '#', '$', '%', '&', '(', ')', '*', '+']
        password_list = ""
        if int(complex) == 1:
            messagebox.showinfo(title="Rule", message="Password contains only characters.")
            password1 = [choice(letters) for _ in range(int(length))]
            password_list = password1
        elif int(complex) == 2:
            messagebox.showinfo(title="Rule", message="Password may contains characters and numbers.")
            password2 =[choice(letters_numbers) for _ in range(int(length))]
            password_list = password2

        elif int(complex) == 3:
            messagebox.showinfo(title="Rule", message="Password may contains characters,numbers and  symbols.")
            password3 =[choice(letters_numbers_symbol) for _ in range(int(length))]
            password_list = password3

        else:
            messagebox.showinfo(title="Oops", message="Kindly choose number between 1 and 3.")

        shuffle(password_list)
        password ="".join(password_list)

        entry3.insert(0, password)




window = Tk()
window.title("Password generator")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)

label1 = Label(text="Desired length")
label1.grid(row=1,column=0)
label2 = Label(text="Complexity(1-3)")
label2.grid(row=2,column=0)
label3 = Label(text="Password")
label3.grid(row=6,column=0)

entry1 = Entry(width=35)
entry1.grid(row=1,column=1)
entry1.focus()
entry2 = Entry(width=35)
entry2.grid(row=2,column=1)
entry3 = Entry(width=21)
entry3.grid(row=6,column=1)

button1 = Button(text="Generate Password",command=generate_password)
button1.grid(row=4,column=1)

window.mainloop()