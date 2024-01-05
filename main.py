from tkinter import *
from tkinter import messagebox
import pandas
import pyperclip

window = Tk()
# window.minsize(width=500, height=500)
window.config(pady=20, padx=20, bg='white')
window.title('password manager')
import random

# characters

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
number_of_letter = random.randint(8, 10)
number_of_number = random.randint(2, 4)
number_of_symbol = random.randint(2, 4)


def generate_password():
    random_letters = [random.choice(letters) for _ in range(number_of_letter)]
    random_numbers = [random.choice(numbers) for _ in range(number_of_number)]
    random_symbol = [random.choice(symbols) for _ in range(number_of_symbol)]

    combined = random_symbol + random_letters + random_numbers
    random.shuffle(combined)
    password_list = ''.join(combined)
    password_entry.insert(0, password_list)
    pyperclip.copy(password_list)


def add_me():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data = {'Name': ['website', 'email', 'password'],
            'Age': [website, email, password]}
    dataframe = pandas.DataFrame(data)

    is_clicked_ok = messagebox.askokcancel(title='Decision', message=f'website: {website}\n email: {email}\n '
                                                                     f'password: {password}')

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Enter Field', message='website or password can\'t be empty')

    elif is_clicked_ok:
        with open('saved_data.txt', mode='a') as f:
            f.write(f'{website_entry.get()}| {email_entry.get()}|{password_entry.get()} \n')
            password_entry.delete(0, END),
            website_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)

website_label = Label(text='Website: ', font=('Aria', 20), bg='white', fg='black')
email_username_label = Label(text='Email/Username: ', font=('Aria', 20), bg='white', fg='black')
password_label = Label(text='Password: ', font=('Aria', 20), bg='white', fg='black')
website_entry = Entry(width=36, bg='white', fg='black')
email_entry = Entry(width=36, bg='white', fg='black')
email_entry.insert(0, 'christopherobinna27@gmail.com')
website_entry.focus()
password_entry = Entry(width=21, bg='white', fg='black')
generate_button = Button(text='Generate password', command=generate_password)
add_button = Button(text='add', width=36, command=add_me)

canvas.grid(column=1, row=0)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
website_entry.grid(column=1, row=1, columnspan=2)
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
