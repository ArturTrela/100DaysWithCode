import tkinter as tk
import tkinter.messagebox

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
CANVA_BG = "#F8FFD2"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = tk.Label(text=f"Score : {self.score} ", font=("Arial", 20, "italic"), bg=THEME_COLOR, fg="White")
        self.score_label.config(padx=20, pady=20, )
        self.score_label.grid(column=1, row=0, sticky=tk.E)

        self.canvas = tk.Canvas()

        self.canvas.config(width=300, height=250, highlightthickness=0,bg=CANVA_BG )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, width=280, text="Temporary",
                                                     font=("Arial", 20, "italic"), fill="Black")

        true_btn = tk.PhotoImage(width=100, height=97, file="true.png")
        self.true_Button = tk.Button(image=true_btn, command=self.right_button, highlightthickness=0)
        self.true_Button.grid(column=0, row=2, sticky=tk.NW)

        wrong_btn = tk.PhotoImage(width=100, height=97, file="false.png")
        self.wrong_Button = tk.Button(image=wrong_btn, command=self.wrong_button, highlightthickness=0)
        self.wrong_Button.grid(column=1, row=2, sticky=tk.NE)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if not self.quiz.still_has_questions():
            tkinter.messagebox.showinfo(title="QUIZ COMPLETE", message="You've completed the quiz\n"
                                        f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
        else :
            self.score_label.config(text=f'Score : {self.quiz.score}')
            self.canvas.config(bg=CANVA_BG)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

    def right_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
