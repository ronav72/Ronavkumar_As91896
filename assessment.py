import tkinter as tk
from PIL import Image, ImageTk



root = tk.Tk()





# Quiz Homepage

#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("850x650")


#opens image
image = Image.open("Intro image .png")
resized_image = image.resize((850,650))
#converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(resized_image)
label = tk.Label(image=img)
#creating label that holds widget inside the window
label.image = img
#label.pack displays that label inside the window
label.pack()



def Start():
    print("Button clicked!")



#creating a button to go to the next page
button = tk.Button(root,
                   text="START",
                   command = Start(),
                   activebackground="light gray",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="#122522",g
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="white",
                   font=("Telegraf", 30),
                   height=2,
                   highlightbackground="black",
                   highlightcolor = "green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=10,
                   width=10,
                   wraplength=100)
button.pack()




























#root.mainloop keeps the window open for events to happen
root.mainloop()