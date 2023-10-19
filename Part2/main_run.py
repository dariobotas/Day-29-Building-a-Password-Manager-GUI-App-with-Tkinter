from tkinter import *


def run():
  window = Tk()
  window.title("Hello world")
  window.config(padx=20, pady=20)

  canvas = Canvas(height=200, width=200)
  logo_img = PhotoImage(file="/home/runner/Day-29-Building-a-Password-Manager-GUI-App-with-Tkinter/logo.png")
  canvas.create_image(100,100, image=logo_img)
  canvas.pack()

  window.mainloop()