from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


#----------------------------- WEBSITE SEARCHER----------------------------------#
def search_website():
    website = website_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
            info = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title="No File Found", message="There is no saved data file.")
    except KeyError:
        messagebox.showinfo(title="Website Missing", message="This website doesn't exist in the data file")
    else:
        email = data[website]["email"]
        pw = data[website]["password"]
        messagebox.showinfo(title=website,message=f"Email:  {email} \nPassword:  {pw}")
        pyperclip.copy(pw)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters  + password_symbol + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=2)
        else:
            # update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #saving updated Data
                json.dump(data, file, indent=2)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()
email_input = Entry(width=60)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "rayspam11@gmail.com")
password_input = Entry(width=40)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add_data, width=50)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search_website, width = 15)
search_button.grid(row=1, column=2)

window.mainloop()