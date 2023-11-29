import tkinter as tk
from quiz_brain import Q_TEXT

THEME_COLOR = "#375362"
CANVA_BG = "#F8FFD2"

question = Q_TEXT
score = 0

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(text=f"Score : {score} ", font=("Arial", 20, "italic"), bg=THEME_COLOR, fg="White")
        self.score_label.config(padx=20, pady=20, )
        self.score_label.grid(column=1, row=0,sticky=tk.E)

        self.canvas = tk.Canvas()

        self.canvas.config(width=300, height=250, highlightthickness=0,)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, text="Temporary Text to Show", font=("Arial", 20, "italic"), fill="Black")

        true_btn = tk.PhotoImage(width=100, height=97, file="true.png")
        self.true_Button = tk.Button(image=true_btn, command='',highlightthickness=0)
        self.true_Button.grid(column=0, row=2,sticky=tk.NW)

        wrong_btn = tk.PhotoImage(width=100, height=97, file="false.png")
        self.wrong_Button = tk.Button(image=wrong_btn, command='',highlightthickness=0)
        self.wrong_Button.grid(column=1, row=2,sticky=tk.NE)

        self.window.mainloop()

    def true_answer(self):
        pass

    def wrong_answer(self):
        pass
