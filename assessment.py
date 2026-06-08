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



root = tk.Tk()

#opens image
image = Image.open("Intro image without button.png")

# converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(image)
label = tk.Label(image=img)
# creating label that holds widget inside the window
label.image = img
#this makes the user unable to resize the height and width
root.resizable( width= "false", height="false")

# label.pack displays that label inside the window
label.pack()



#title of gui window
root.title("New Zealand History Quiz")

#setting geometry of gui window
root.geometry("1200x650")



#adding an image as a button for my homepage
entry_button = tk.PhotoImage (file="homepage button.png")
button =tk.Button(root, image=entry_button)
#placing the button in the center, just below the entry box
button.place(relx=0.47, rely=0.73, anchor="center")


#this displays a text above the entry box saying please enter your username in the box below
text_entrybox = tk.Label(root, text="Please enter your username in the box below")
text_entrybox.place(relx=0.38, rely=0.5)


#storing the users name
def valid_user():
    name = names_entrybox.get()
    if any(char.isdigit() for char in names):
        text_entrybox.config(text="You can not have any numbers in your name", fg="red")




#adding an entry box for the user to enter their name
names_entrybox = tk.Entry (root, bd=2.5, width=30)
names_entrybox.place(relx=0.47, rely=0.58, anchor="center")# placing it in the center
button.config(command=valid_user) #checking the users name when clicking the button

names_entrybox.bind("Return", lambda event: valid_user()) # this makes it so when the user presses enter it checks their name






#root.mainloop keeps the window open for events to happen
root.mainloop()