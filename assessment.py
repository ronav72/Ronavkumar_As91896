import tkinter as tk
from string import whitespace
from tkinter import PhotoImage
from PIL import Image, ImageTk


names = []  # This will keep track of players' names
score = 0
relevant_question_index = 0


# This is the questions and answers that the user will see / be asked in the second page
questions_answers = [
   {"question 1": "When did Moari first arrive in New Zealand?", "choices 1": ["1250 CE", "3000bc", "1875", "1920"],
    "answer 1": "1250 CE", "background 1": "question one background.png"},
   {"question 2": "How many tourists lost their lives from the white island volcano eruption?",
    "choices 2": ["22 people", "25 people", "43 people", "67 people"],
    "answer 2": "22 people lost their lives, and about 25 others were injured as well",
    "background 2": "question two background.png"},
   {
       "question 3": "During the 2023 flooding, there was a record-breaking amount of rainfall in the upper north island region. How much rainfall was recorded to be spread across the North Island?",
       "choices 3": ["278mm", "539mm", "300mm", "265mm"], "answer 3": "265mm",
       "background 3": "question three background.png"},
   {"question 4": "What is the name of the largest wildfire in New Zealand?",
    "choices 4": ["Lake Ohau fire", "Pigeon Valley Fire", "Lake Pukaki", "Taranaki Wildfire"],
    "answer 4": "Lake Ohau fire", "background 4": "question four background.png"},
   {
       "question 5": "On 28 November 1979, an Air New Zealand aircraft crashed into the lower slopes of Mt Erebus with an carrying amount of 257 people on board including crew , named the Mount Erebus disaster. How many people died from this crash?",
       "choices 5": ["All 257 passengers", "200 passengers", "158 passengers", "No one, everyone survived"],
       "answer 5": "All 257 passengers", "background 5": "question five background.png"},
   {"question 6": "Who signed the Treaty of Waitangi from the British side?",
    "choices 6": ["Andrew Gibson", "Gilbert Walker", "Richie Shepard", "William Hobson"],
    "answer 6": "William Hobson", "background 6": "question six background.png"},
   {
       "question 7": "A New Zealander was the first person to climb Mt Everest. He later appeared on the 5$ bill. What was this New Zealander's name?",
       "choices 7": ["Taikawaititi junior", "Lewis Dod", "George Calvin", "Edmund Hillary"],
       "answer 7": "Edmund Hillary", "background 7": "question seven background.png"},
   {"question 8": "The largest lake in New Zealand is Lake Taupo. It was formed 25,000 years ago. How was it made?",
    "choices 8": ["A meteor hit it and created a massive hole", "Taupo Volcano",
                  " A series of volcanic eruptions caused the lake to form", "Many people dug it up"],
    "answer 8": " A series of volcanic eruptions caused the lake to form",
    "background 8": "question eight background.png"},
   {
       "question 9": " Bungee jumping was originally made in New Zealand. It is when you jump off from a high elevation down towards the ground with an elastic cord connected. Who is responsible for this invention?",
       "choices 9": ["Malachy Goodman", "Carlo Phillip", "A.J Hackett", "Henery O Donald"], "answer 9": "A.J Hackett",
       "background 9": "question nine background.png"},
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




names_entrybox = tk.Entry(root, bd=2.5, width=30)# This displays a text above the entry box saying please enter your username in the box below
text_entrybox = tk.Label(root, text="Please enter your username in the box below") #this creates a label called text_entry box
text_entrybox.place(relx=0.38, rely=0.5) #displays the entrybox label




def open_questions_page():  # Creating the second component of the quiz
   root.withdraw()
   start_page = tk.Toplevel()  # the code Toplevel opens a new window
   start_page.title("Questions") #the title of this page is going to be called "Questions"
   start_page.geometry("1200x650") #this changes the geometry to 1200x 650




   question_1 = questions_answers[relevant_question_index]
   bg_key = f"background {relevant_question_index + 1}" #circles through the background images and adds 1 to it each time the user press next
   bg_filename = question_1[bg_key]


   image = Image.open(bg_filename)
   img = ImageTk.PhotoImage(image) #converts the photo into a file tkinter can understand
   label_background_image = tk.Label(start_page, image=img) #creates a label for the background image
   start_page.bg_image = img
   label_background_image.pack() #this displays the label (label_background_image)


   root.resizable(width="false", height="false") #makes the height and width of the program fixed so the user can change it




   questions_text = question_1[f"question {relevant_question_index + 1}"] #this adds 1 to the current question and does this until the final question


   questions_label = tk.Label(start_page, text=questions_text, font=("Roboto", 22, "bold"))
   questions_label.place(relx=0.5, rely=0.15, anchor="center")


   options = question_1[f"choices {relevant_question_index + 1}"]




   def open_last_page():
       end_page = tk.Toplevel()
       end_page.title("Quiz Done")
       end_page.geometry("1200x650")
       end_page.resizable(width="false", height="false")


       image_end = Image.open("final quiz background.png")
       img_end = ImageTk.PhotoImage(image_end)
       label_end_background = tk.Label(end_page, image=img_end)
       end_page.bg_image = img_end
       label_end_background.pack()


       player_name = names[-1] if names else "Player"
       final_results_text = f"Congratulations {player_name}!\nYou have finished the Quiz!\n\nFinal Score: {score} / {len(questions_answers)}"


       results_label = tk.Label(end_page, text=final_results_text, font=("Roboto", 25, "bold"), fg="white",
                                bg="#2c3e50", justify="center")
       results_label.place(relx=0.5, rely=0.5, anchor="center")


   def goto_next_question():
       global relevant_question_index
       relevant_question_index += 1
       if relevant_question_index < len(questions_answers):
           start_page.destroy()
           open_questions_page()
       else:
           start_page.destroy()
           open_last_page()  # Resolves perfectly now!


   next_question_button = tk.Button(start_page, text="Next Question", font=("Helvetica", 20, "bold"),
                                    command=goto_next_question)


   def answer_check(user_choice):
       global score
       label_responce.place(relx=0.5, rely=0.45, anchor="center")


       answer_correct = question_1[f"answer {relevant_question_index + 1}"]
       if user_choice == answer_correct:
           label_responce.config(text="Well done your answer is Correct!", fg="green")
           score += 1
       else:
           label_responce.config(text="Sorry, your answer is Incorrect! Better luck next time!", fg="red")


       button_1.config(command=lambda: None)
       button_2.config(command=lambda: None)
       button_3.config(command=lambda: None)
       button_4.config(command=lambda: None)


       next_question_button.place(relx=0.5, rely=0.88, anchor="center")


   button_1 = tk.Button(start_page, text=options[0], width=30, command=lambda: answer_check(options[0]))
   button_1.place(relx=0.37, rely=0.73, anchor="center")

   button_2 = tk.Button(start_page, text=options[1], width=30, command=lambda: answer_check(options[1]))
   button_2.place(relx=0.37, rely=0.78, anchor="center")

   button_3 = tk.Button(start_page, text=options[2], width=35, command=lambda: answer_check(options[2]))
   button_3.place(relx=0.60, rely=0.73, anchor="center")

   button_4 = tk.Button(start_page, text=options[3], width=35, command=lambda: answer_check(options[3]))
   button_4.place(relx=0.60, rely=0.78, anchor="center")

   label_responce = tk.Label(start_page, text="", font=("Roboto", 24, "bold"), bg="#5A8F9D")




#defining a new function and this checks if the users name is valid or not
def valid_user():
   name = names_entrybox.get()
   if any(char.isdigit() for char in name): #this checks if there is numbers in the users name
       text_entrybox.config(text="You can not have any numbers in your name", fg="red") # if the users name does have a number or numbers in it then a message will pop up saying that "You can not have any numbers in your name" in red text
   elif name.strip() == "": #this checks if the user has entered a name or just nothing
       text_entrybox.config(text="Please enter your name", fg="red") #if they have entered nothing then a message will say "please enter your name" in red
   else:
       text_entrybox.config(text="welcome to the quiz", fg="green") #if the name meets both of the conditions then the text will say "welcome to the quiz" in green
       names.append(name)
       root.after(1300, open_questions_page) #this will open the question page after 1.3 seconds
       button.config(command=lambda: None) #after the button is pressed this will disable it from making users opening multiple new windows






names_entrybox.place(relx=0.47, rely=0.58, anchor="center") #this places the entrybox


#the button is linked to function valid_user and when the user clicks the button then it checks if the name meets the two conditions
button.config(command=valid_user)




names_entrybox.bind("<Return>", lambda event: valid_user()) #this binds the enter button your keyboard to a mouse click


#this runs the program and keeps it from shutting down
root.mainloop()



