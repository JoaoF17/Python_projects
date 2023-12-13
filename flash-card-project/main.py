from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Fetch words from CSV file ------------------------------- #
try:
  data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# ---------------------------- Unknown Button to change words ------------------------------- #
def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = choice(to_learn)
  canvas.itemconfig(title, text="French", fill="black")
  canvas.itemconfig(word, text=current_card["French"], fill="black")
  canvas.itemconfig(card_background, image=card_front)
  flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Known Button to change words ------------------------------- #
def is_known():
  to_learn.remove(current_card)
  print(len(to_learn))
  df = pd.DataFrame(to_learn)
  df.to_csv("data/words_to_learn.csv", index=False)
  next_card()

# ---------------------------- Flip Card Function ------------------------------- #
def flip_card():
  canvas.itemconfig(card_background, image=card_back)
  canvas.itemconfig(title, text="English", fill="white")
  canvas.itemconfig(word, text=current_card["English"], fill="white")

# ---------------------------- UI Interface ------------------------------- #
#window creation
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#card image; canvas
canvas = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 268, image=card_front)

#Canvas text
title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

#right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=is_known, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

next_card()


window.mainloop()