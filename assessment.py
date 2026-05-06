import tkinter as tk

root = tk.Tk

#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("500x560")

#background image of the homepage
bg = tk.PhotoImage(file="Intro image .png")

#creating label, holds widget inside the window
label= tk.Label(image=bg)
label.pack()

root.mainloop()