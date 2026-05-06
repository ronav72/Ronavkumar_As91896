import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk

#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("2000x3000")

#background image of the homepage
bg = tk.PhotoImage(file="Intro image .png")

#creating label that holds widget inside the window
label= tk.Label(image=bg)
#label.pack displays that label inside the window
label.pack()

image = Image.open("Intro image .png")
resized_image = image.resize((50,50))
#converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(resized_image)
label = tk.Label(image=img)
label.image = img
label.pack()




#root.mainloop keeps the window open for events to happen
root.mainloop()