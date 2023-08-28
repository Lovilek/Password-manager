from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generat_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]

    password_list += (random.choice(symbols) for i in range(random.randint(2, 4)))

    password_list += (random.choice(numbers) for i in range(random.randint(2, 4)))

    random.shuffle(password_list)

    password = "".join(password_list)

    if not entry_pas:
        entry_pas.insert(0, password)
    else:
        entry_pas.delete(0, END)
        entry_pas.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {
        entry_web.get(): {
            "email": entry_em_us.get(),
            "password": entry_pas.get()
        }
    }
    if not entry_pas.get() or not entry_web.get() or not entry_em_us.get():
        messagebox.showwarning(title="Warning", message="Don't leave any fields empty")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        entry_pas.delete(0, END)
        entry_web.delete(0, END)


# ---------------------------- Search ------------------------------- #

def search():
    if not entry_web.get():
        messagebox.showwarning(title="Warning", message="Don't leave field empty")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                if entry_web.get() in data:
                    messagebox.showinfo(title=entry_web.get(),
                                        message=f"Email: {data[entry_web.get()]['email']}\nPassword: {data[entry_web.get()]['password']}")
                else:
                    messagebox.showwarning(title="Warning", message="No details for the website exists")
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label_web = Label(text="Website:")
label_web.grid(row=1, column=0)
label_em_us = Label(text="Email/Username:")
label_em_us.grid(row=2, column=0)
label_pas = Label(text="Password:")
label_pas.grid(row=3, column=0)

button_gen_pas = Button(text="Generate Password", command=generat_password)
button_gen_pas.grid(row=3, column=2)
button_add = Button(text="Add", width=44, command=save)
button_add.grid(row=4, column=1, columnspan=2)
button_search = Button(text="Search", width=14, command=search)
button_search.grid(row=1, column=2)

entry_web = Entry(width=34)
entry_web.grid(row=1, column=1)
entry_web.focus()
entry_em_us = Entry(width=52)
entry_em_us.grid(row=2, column=1, columnspan=2)
entry_pas = Entry(width=34)
entry_em_us.insert(0, "wingeddemon2274@gmail.com")
entry_pas.grid(row=3, column=1)

window.mainloop()
