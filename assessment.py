import tkinter as tk
from PIL import Image, ImageTk
names=[] #this will keep track of players names

#this is the questions and answers that the user will see / be asked in the second page
questions_answers = [
    {"question": "When did Moari first arrive in New Zealand?", "choices": ["1250 CE", "3000bc", "1875", "1920"], "answer": "1250 CE"},
    {"question": "How many tourists lost their lives from the white island volcano eruption?", "choices": ["22 people", "25 people", "43 people", "67 people"],"answer": "22 people lost their lives, and about 25 others were injured as well"},
    {"question": "During the 2023 flooding, there was a record-breaking amount of rainfall in the upper north island region. How much rainfall was recorded to be spread across the North Island?",
     "choices": ["278mm", "539mm", "300mm", "265mm"],"answer": "265mm"},
    {"question": "What is the name of the largest wildfire in New Zealand?", "choices": ["Lake Ohau fire", "Pigeon Valley Fire", "Lake Pukaki", "Taranaki Wildfire"],
     "answer": "Lake Ohau fire"},
    {"question": "On 28 November 1979, an Air New Zealand aircraft crashed into the lower slopes of Mt Erebus with an carrying amount of 257 people on board including crew , named the Mount Erebus disaster. How many people died from this crash?",
     "choices": ["All 257 passengers", "200 passengers", "158 passengers", "No one, everyone survived"], "answer": "All 257 passengers"},
    {"question": "Who signed the Treaty of Waitangi from the British side?", "choices": ["Andrew Gibson", "Gilbert Walker", "Richie Shepard", "William Hobson"], "answer": "William Hobson"},
    {"question": "A New Zealander was the first person to climb Mt Everest. He later appeared on the 5$ bill. What was this New Zealander's name?", "choices": ["Taikawaititi junior", "Lewis Dod", "George Calvin", "Edmund Hillary"],
     "answer": "Edmund Hillary"},
    {"question": "The largest lake in New Zealand is Lake Taupo. It was formed 25,000 years ago. How was it made?", "choices": ["A meteor hit it and created a massive hole", "Taupo Volcano", " A series of volcanic eruptions caused the lake to form", "Many people dug it up"],
     "answer": " A series of volcanic eruptions caused the lake to form"},
    {"question": " Bungee jumping was originally made in New Zealand. It is when you jump off from a high elevation down towards the ground with an elastic cord connected. Who is responsible for this invention?",
     "choices": ["Malachy Goodman", "Carlo Phillip", "A.J Hackett", "Henery O Donald"],
     "answer": "A.J Hackett"},
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