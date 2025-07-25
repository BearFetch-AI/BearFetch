import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App with Score Tracking")
        self.root.geometry("650x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#97704F")  # main background

        # Color palette
        self.bg_color = "#97704F"
        self.card_color = "#F8EFE7"
        self.primary_text = "#3E2C23"
        self.accent_color = "#D9A066"
        self.hover_color = "#B67C3B"
        self.restart_color = "#6E4B2A"
        self.restart_hover = "#5C3E22"

        # Quiz data
        self.questions = [
            {"question": "What is the capital of France?",
             "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What planet is known as the Red Planet?",
             "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
            {"question": "What is 5 + 7?",
             "options": ["10", "12", "11", "13"], "answer": "12"},
            {"question": "Who wrote 'Romeo and Juliet'?",
             "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
            {"question": "Which is the largest ocean on Earth?",
             "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"}
        ]

        self.score = 0
        self.q_index = 0

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.card = tk.Frame(self.root, bg=self.card_color, bd=2, relief="ridge")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=580, height=360)

        self.question_label = tk.Label(
            self.card, text="", font=("Georgia", 16, "bold"), wraplength=500,
            fg=self.primary_text, bg=self.card_color, justify="left"
        )
        self.question_label.pack(pady=20, anchor="w", padx=20)

        self.var = tk.StringVar(value="")
        self.radio_buttons = []

        for _ in range(4):
            rb = tk.Radiobutton(
                self.card, text="", variable=self.var, value="",
                font=("Georgia", 13), bg=self.card_color, fg=self.primary_text,
                activebackground=self.card_color, activeforeground=self.accent_color,
                selectcolor="#EEDDCB", anchor="w", padx=20
            )
            rb.pack(anchor='w', padx=20, pady=3)
            self.radio_buttons.append(rb)

        self.progress_label = tk.Label(
            self.card, text="", font=("Georgia", 11), fg=self.primary_text, bg=self.card_color
        )
        self.progress_label.pack(pady=(10, 0))

        self.score_label = tk.Label(
            self.card, text="Score: 0", font=("Georgia", 11, "bold"),
            fg=self.accent_color, bg=self.card_color
        )
        self.score_label.pack()

        self.btn_frame = tk.Frame(self.card, bg=self.card_color)
        self.btn_frame.pack(pady=15)

        self.next_btn = self.create_button(self.btn_frame, "Next", self.next_question, self.accent_color, self.hover_color)
        self.next_btn.grid(row=0, column=0, padx=10)

        self.restart_btn = self.create_button(self.btn_frame, "Restart", self.restart_quiz, self.restart_color, self.restart_hover)
        self.restart_btn.grid(row=0, column=1, padx=10)

    def create_button(self, parent, text, command, bg_color, hover_color):
        btn = tk.Button(
            parent, text=text, command=command,
            font=("Georgia", 11), bg=bg_color, fg="black",
            activebackground=hover_color, width=12, height=2, bd=0
        )
        # Add hover animation
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        return btn

    def load_question(self):
        q = self.questions[self.q_index]
        self.question_label.config(text=q["question"])
        self.var.set("")

        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option)

        self.progress_label.config(
            text=f"Question {self.q_index + 1} of {len(self.questions)}")
        self.score_label.config(text=f"Score: {self.score}")

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an option before proceeding.")
            return

        if selected == self.questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1

        if self.q_index >= len(self.questions):
            self.show_summary_screen()
        else:
            self.load_question()

    def show_summary_screen(self):
        # Clear the card and show a summary
        for widget in self.card.winfo_children():
            widget.destroy()

        summary_title = tk.Label(
            self.card, text="Quiz Summary", font=("Georgia", 18, "bold"),
            fg=self.primary_text, bg=self.card_color
        )
        summary_title.pack(pady=(30, 10))

        summary_msg = f"You scored {self.score} out of {len(self.questions)}."
        summary_label = tk.Label(
            self.card, text=summary_msg, font=("Georgia", 14),
            fg=self.primary_text, bg=self.card_color
        )
        summary_label.pack(pady=10)

        restart_btn = self.create_button(self.card, "Restart Quiz", self.restart_quiz, self.restart_color, self.restart_hover)
        restart_btn.pack(pady=20)

    def restart_quiz(self):
        self.score = 0
        self.q_index = 0

        # Clear current content
        for widget in self.card.winfo_children():
            widget.destroy()

        self.create_widgets()
        self.load_question()

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
