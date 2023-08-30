import tkinter as tk
from tkinter import ttk
import random

class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("600x400")

        self.keywords = ["plastic", "pollution", "ocean", "marine", "rahui", "microplastics", "recycle", "waste", "ecosystem", "tangaroa"]

        self.reset_game()

        self.hangman_label = ttk.Label(self.master, text=self.display_hangman())
        self.hangman_label.pack()

        self.word_label = ttk.Label(self.master, text=" ".join(self.word_completion))
        self.word_label.pack()

        self.buttons_frame = ttk.Frame(self.master)
        self.buttons_frame.pack()

        for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            button = ttk.Button(self.buttons_frame, text=letter.upper(), command=lambda l=letter: self.make_guess(l))
            button.grid(row=idx // 13, column=idx % 13)

    def reset_game(self):
        self.word = random.choice(self.keywords)
        self.word_completion = ["_"] * len(self.word)
        self.guessed_letters = []
        self.tries = 7

    def make_guess(self, letter):
        pass  # Implement your guessing logic here

    def display_hangman(self):
        stages = ["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5", "Stage 6", "Stage 7"]
        return stages[self.tries] if self.tries < len(stages) else "Game Over"

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
