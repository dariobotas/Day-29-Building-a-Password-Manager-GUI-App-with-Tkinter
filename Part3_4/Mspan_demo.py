from tkinter import *


def run():
  window = Tk()
  window.title("Hello world")
  window.config(padx=20, pady=20)

  r = Label(bg="red", width=20, height=5)
  r.grid(row=0, column=0)

  g = Label(bg="green", width=20, height=5)
  g.grid(row=1, column=1)

  #b = Label(bg="blue", width=20, height=5)
  #b.grid(row=2, column=0)
  b = Label(bg="blue", width=40, height=5)
  b.grid(row=2, column=0, columnspan=2)
  
  window.mainloop()