from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    #pick the question from quiz_brain
    self.quiz = quiz_brain
    #build the window
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    #Score
    self.score = Label(text="Score = 0", padx=20, pady=20, bg=THEME_COLOR)
    self.score.grid(column=1, row=0)
    #Canvas for Question
    self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
    self.question_text = self.canvas.create_text(
      150,
      125,
      width=280,
      text="random text",
      fill=THEME_COLOR,
      font=("Arial", 20, "italic")
      )
    self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
    #true button
    true_image = PhotoImage(file="images/true.png")
    self.true_button = Button(image=true_image, command=self.true_pressed, highlightbackground=THEME_COLOR, highlightcolor=THEME_COLOR) #add command
    self.true_button.grid(column=0, row=2)
    #wrong button
    wrong_image = PhotoImage(file="images/false.png")
    self.wrong_button = Button(image= wrong_image, command=self.false_pressed, highlightbackground=THEME_COLOR, highlightcolor=THEME_COLOR) #add command
    self.wrong_button.grid(column=1, row=2)
    
    self.get_next_question()
    
    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      self.score.config(text=f"Score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text= q_text)
    else:
      self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
      self.true_button.config(state="disabled")
      self.wrong_button.config(state="disabled")
    
  def true_pressed(self):
    self.give_feedback(self.quiz.check_answer("True"))
    
  def false_pressed(self):
    self.give_feedback(self.quiz.check_answer("True"))
  
  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)