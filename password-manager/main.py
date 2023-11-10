from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  pass_letters = [choice(letters) for _ in range(randint(8, 10))]
  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))

  pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)

  pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)

  password_list = pass_letters + pass_numbers + pass_symbols
  shuffle(password_list)

  password = "".join(password_list) #join instead of the for loop
  # password = ""
  # for char in password_list:
  #   password += char

  print(f"Your password is: {password}")
  password_entry.insert(0, string=password)
  copy(password) #add created passwrod to the copy clipboard
  
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
  website = website_entry.get()
  username = user_entry.get()
  password = password_entry.get()
  
  if len(website) == 0 or len(username) == 0 or len(password) == 0: #boxes left blank
    messagebox.showinfo(title="Warning", message="You left a field in blank")
  else: #confirm details
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password}")
    
    if is_ok:
      with open("password.txt", mode="a") as password_file:
        password_file.write(f"{website} || {username} || {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#window creation
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

#get bg image
canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

#Website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus() #cursor will be in this field upon app start

#user label and entry
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_entry = Entry()
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(0, "joao@hotmail.com")

#Password
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=generate_pass)
password_button.grid(column=2, row=3, sticky="EW")

#add button
add_button = Button(text="Add", width=35, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()