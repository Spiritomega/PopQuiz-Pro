from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="some text", width=280,
                                                   font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_button_img = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=correct_button_img, highlightthickness=0, command=self.correct_button_press)
        self.correct_button.grid(row=2, column=0)

        wrong_button_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=self.wrong_button_press)
        self.wrong_button.grid(row=2, column=1)

        self.display_question()

        self.window.mainloop()

    def display_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self.canvas.itemconfig(self.canvas_text, text= "You've reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_button_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_button_press(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_question)

