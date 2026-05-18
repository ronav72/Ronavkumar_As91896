import tkinter as tk
from PIL import Image, ImageTk
names=[] #this will keep track of players names












root = tk.Tk()

# Making a Frame to hold widgets
frame=tk.Frame(root, padx=100, pady=100)
frame.pack(padx=100, pady=100)


# Quiz Homepage

#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("850x650")


#opens image
image = Image.open("Intro image without button.png")
resized_image = image.resize((850,650))
#converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(resized_image)
label = tk.Label(image=img)
#creating label that holds widget inside the window
label.image = img
#label.pack displays that label inside the window
label.place(relx=0.5, rely=0.5,anchor="center" )

button=tk.Button(root, text="Continue")
button.pack(pady=100, padx=100,     )
#placing the buttons positon
button.place(x=400, y=500)























#root.mainloop keeps the window open for events to happen
root.mainloop()