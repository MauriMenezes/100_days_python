from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'score : 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text=f'some text', fill=THEME_COLOR, font=('Arial', 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score : {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text=f'Your score was {self.quiz.score} correct answers')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def is_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_rigth):
        if is_rigth:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
