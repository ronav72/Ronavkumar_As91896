import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()





# Quiz Homepage

#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("850x650")



image = Image.open("Intro image .png")
resized_image = image.resize((850,650))
#converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(resized_image)
label = tk.Label(image=img)
#creating label that holds widget inside the window
label.image = img
#label.pack displays that label inside the window
label.pack()
































#root.mainloop keeps the window open for events to happen
root.mainloop()