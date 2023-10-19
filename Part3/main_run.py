from tkinter import *


def run():
  # ---------------------------- PASSWORD GENERATOR ------------------------------- #

  # ---------------------------- SAVE PASSWORD ------------------------------- #

  # ---------------------------- UI SETUP ------------------------------- #
  
  window = Tk()
  window.title("Hello world")
  window.config(padx=50, pady=50, bg="white")

  canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
  logo_img = PhotoImage(file="/home/runner/Day-29-Building-a-Password-Manager-GUI-App-with-Tkinter/logo.png")
  canvas.create_image(100,100, image=logo_img)
  canvas.grid(row=0, column=1)

  #Labels
  website_label = Label(text="Website:", bg="white")
  website_label.grid(row=1,column=0)

  email_username_label = Label(text="Email/Username:", bg="white")
  email_username_label.grid(row=2,column=0)

  password_label = Label(text="Password:", bg="white")
  password_label.grid(row=3,column=0)

  #Entries
  website_entry = Entry(width=35, highlightthickness=0)
  website_entry.grid(row=1,column=1, columnspan=2, sticky="w")

  email_username_entry = Entry(width=35, highlightthickness=0)
  email_username_entry.grid(row=2,column=1, columnspan=2, sticky="w")

  password_entry = Entry(width=21, highlightthickness=0)
  password_entry.grid(row=3,column=1, sticky="w")

  #Buttons
  generate_password_button = Button(text="Generate Password", command=lambda: print("Hello"), bg="white")
  generate_password_button.grid(row=3,column=2, sticky="w")

  add_button = Button(text="Add", command=lambda: print("Hello"), width=36, bg="white")
  add_button.grid(row=4,column=1, columnspan=2, sticky="w")

  window.mainloop()