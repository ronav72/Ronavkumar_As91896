import tkinter as tk
from PIL import Image, ImageTk
names=[] #this will keep track of players names


quiz_data = [
    {"question": "When did Moari first arrive in New Zealand?", "choices": ["1250 CE", "3000bc", "1875", "1920"], "answer": "1250 CE"},
    {"question": "How many tourists lost their lives from the white island volcano eruption?", "choices": ["22 people", "25 people", "1875", "1920"],"answer": "1250 CE"},

]


#creating a class (a class is a blueprint or template which is used to create objects)

class Homepage:
    def __init__(self, parent):
        self.quiz_frame = tk.Frame (parent, padx=100, pady=100)
        self.quiz_frame.place(relx=0.5,rely=0.5,anchor="center")

#text to display above the entry box
        self.user_label= tk.Label (self.quiz_frame,text="enter your name", font=("Tw Cen Mt", "16"))
        self.user_label.grid()


#creating a entry box for the user to enter their name
        self.entry_box = tk.Entry(self.quiz_frame)
        self.entry_box.grid()


#making a start button for when the user is finished entering their name, they are able to start the program and go the next page
        self.start_button = tk.Button(self.quiz_frame, text="START",command=self.name_collector)
        self.start_button.grid()


    def name_collector(self):
        global name
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        self.entry_box(root)





if __name__ =="__main__":
    root = tk.Tk()

#opens image
image = Image.open("Intro image without button.png")
resized_image = image.resize((850, 650))
# converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(resized_image)
label = tk.Label(image=img)
# creating label that holds widget inside the window
label.image = img
# label.pack displays that label inside the window
label.place(relx=0.5, rely=0.5, anchor="center")




#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("850x650")

NewZealand_instance =Homepage(root)







#root.mainloop keeps the window open for events to happen
root.mainloop()