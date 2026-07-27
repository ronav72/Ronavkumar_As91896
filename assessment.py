import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


names = []  # This will keep track of players' names


# This is the questions and answers that the user will see / be asked in the second page
questions_answers = [
   {"question 1": "When did Moari first arrive in New Zealand?", "choices 1": ["1250 CE", "3000bc", "1875", "1920"], "answer 1": "1250 CE"},
   {"question 2": "How many tourists lost their lives from the white island volcano eruption?", "choices 2": ["22 people", "25 people", "43 people", "67 people"], "answer 2": "22 people lost their lives, and about 25 others were injured as well"},
   {"question 3": "During the 2023 flooding, there was a record-breaking amount of rainfall in the upper north island region. How much rainfall was recorded to be spread across the North Island?", "choices 3": ["278mm", "539mm", "300mm", "265mm"], "answer 3": "265mm"},
   {"question 4": "What is the name of the largest wildfire in New Zealand?", "choices 4": ["Lake Ohau fire", "Pigeon Valley Fire", "Lake Pukaki", "Taranaki Wildfire"], "answer 4": "Lake Ohau fire"},
   {"question 5": "On 28 November 1979, an Air New Zealand aircraft crashed into the lower slopes of Mt Erebus with an carrying amount of 257 people on board including crew , named the Mount Erebus disaster. How many people died from this crash?", "choices 5": ["All 257 passengers", "200 passengers", "158 passengers", "No one, everyone survived"], "answer 5": "All 257 passengers"},
   {"question 6": "Who signed the Treaty of Waitangi from the British side?", "choices 6": ["Andrew Gibson", "Gilbert Walker", "Richie Shepard", "William Hobson"], "answer 6": "William Hobson"},
   {"question 7": "A New Zealander was the first person to climb Mt Everest. He later appeared on the 5$ bill. What was this New Zealander's name?", "choices 7": ["Taikawaititi junior", "Lewis Dod", "George Calvin", "Edmund Hillary"], "answer 7": "Edmund Hillary"},
   {"question 8": "The largest lake in New Zealand is Lake Taupo. It was formed 25,000 years ago. How was it made?", "choices 8": ["A meteor hit it and created a massive hole", "Taupo Volcano", " A series of volcanic eruptions caused the lake to form", "Many people dug it up"], "answer 8": " A series of volcanic eruptions caused the lake to form"},
   {"question 9": " Bungee jumping was originally made in New Zealand. It is when you jump off from a high elevation down towards the ground with an elastic cord connected. Who is responsible for this invention?", "choices 9": ["Malachy Goodman", "Carlo Phillip", "A.J Hackett", "Henery O Donald"], "answer 9": "A.J Hackett"},
]


root = tk.Tk()


# Opens image
image = Image.open("Intro image without button.png")


# Converts the image into a format Tkinter can understand
img = ImageTk.PhotoImage(image)
label = tk.Label(image=img)
# Creating label that holds widget inside the window
label.image = img
# This makes the user unable to resize the height and width
root.resizable(width="false", height="false")


# Label.pack displays that label inside the window
label.pack()


# Title of gui window
root.title("New Zealand History Quiz")


# Setting geometry of gui window
root.geometry("1200x650")


# Adding an image as a button for my homepage
entry_button = tk.PhotoImage(file="homepage start button.png")
button = tk.Button(root, image=entry_button)
# Placing the button in the center, just below the entry box
button.place(relx=0.47, rely=0.73, anchor="center")


# This displays a text above the entry box saying please enter your username in the box below
names_entrybox = tk.Entry(root, bd=2.5, width=30)
text_entrybox = tk.Label(root, text="Please enter your username in the box below")
text_entrybox.place(relx=0.38, rely=0.5)




def open_questions_page():  # Creating the second component of the quiz
   root.withdraw() #root.withdraw makes it so when the users name matches the requirements it opens a new window and closes the previous window
   start_page = tk.Toplevel()  # Creates the questions and answers page
   start_page.title("Questions")
   start_page.geometry("1200x650")

   image = Image.open("question one background.png")

   img = ImageTk.PhotoImage(image)
   label_background_image = tk.Label (start_page, image=img)
   start_page.bg_image = img
   label_background_image.pack()

   root.resizable(width="false", height="false")


   question_1 = questions_answers [0]
   questions_text = question_1 ["question 1"]

   questions_label = tk.Label(start_page, text=questions_text, font=("Roboto",22, "bold",) )
   questions_label.place(relx=0.5, rely=0.15, anchor="center")

   options = question_1["choices 1"]

   def answer_check(user_choice):
      answer_correct = question_1["answer 1"]
      if user_choice == answer_correct:
         label_responce.config(text="Well done your answer is Correct!", fg="green")
      else:
         label_responce.config(text="Sorry, your answer is Incorrect! Better luck next time!", fg="red")
      button_1.config(command=lambda:None)
      button_2.config(command=lambda:None)
      button_3.config(command=lambda:None)
      button_4.config(command=lambda:None)



   button_1 = tk.Button (start_page, text=options [0], width=30, command=lambda:answer_check(options[0]))
   button_1.place(relx=0.37,rely=0.73, anchor="center")

   button_2 = tk.Button (start_page, text=options [1], width=30, command=lambda: answer_check(options[1]))
   button_2.place(relx=0.37, rely=0.78, anchor="center")

   button_3 = tk.Button(start_page, text=options[2], width=35, command=lambda:answer_check(options[2]))
   button_3.place(relx=0.60, rely=0.73, anchor="center")

   button_4 = tk.Button(start_page, text=options[3], width=35, command=lambda:answer_check(options [3]))
   button_4.place(relx=0.60, rely=0.78, anchor="center")

   label_responce = tk.Label(start_page, text="", font=("Roboto", 24, "bold"))
   label_responce.place(relx=0.5, rely=0.87, anchor="center")


# Storing the users name
def valid_user():
   name = names_entrybox.get()
   if any(char.isdigit() for char in name):
       text_entrybox.config(text="You can not have any numbers in your name", fg="red")
       # If user enters their name with numbers in it, it will show an error message
   elif name.strip() == "":
       text_entrybox.config(text="Please enter your name", fg="red")
       # If user doesn't enter their name and just clicks submit then it will show an error message
   else:
       text_entrybox.config(text="welcome to the quiz", fg="green")
       # If the users name meets the requirements then it will take them to the next page
       root.after(1300, open_questions_page)
       button.config(command=lambda: None)
       # Program waits 2 seconds before opening a new tab








# Placing entry box in the center
names_entrybox.place(relx=0.47, rely=0.58, anchor="center")


# Checking the users name when clicking the button
button.config(command=valid_user)


# This makes it so when the user presses enter it checks their name
names_entrybox.bind("<Return>", lambda event: valid_user())


# Root.mainloop keeps the window open for events to happen
root.mainloop()

