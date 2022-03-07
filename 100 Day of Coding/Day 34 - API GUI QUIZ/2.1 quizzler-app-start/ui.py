from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):

    def __int__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        font = ("Ariel", 20, "italic")
        self.question_box = Canvas(height=250, width=300, bg="white")
        self.question_box.create_text(
            150,
            125,
            text="Text Here",
            fill=THEME_COLOR,
            font=font,
            width=280
        )
        self.question_box.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.respond_true)
        self.check_button.grid(row=2, column=0)

        x_img = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_img, highlightthickness=0, command=self.respond_false)
        self.x_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.question_box.itemconfig(self.question_box, text=q_text, bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
        else:
            self.question_box.itemconfig(self.question_box, text="Quiz is finished!")
            self.respond_true.config(state="disabled")
            self.respond_false.config(state="disabled")

    def respond_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def respond_false(self):
        is_right = self.quiz.check_answer("False")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)