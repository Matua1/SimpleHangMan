import tkinter as tk
from tkinter import ttk
import random

class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("600x400")
        
        self.tries = 7
        self.reset_game()
        self.keywords = ["plastic", "pollution", "ocean", "marine", "rahui", "microplastics", "recycle", "waste", "ecosystem", "tangaroa"]
        

        self.hangman_label = ttk.Label(self.master, text=self.display_hangman())
        self.hangman_label.pack()

        self.word_label = ttk.Label(self.master, text=" ".join(self.word_completion))
        self.word_label.pack()

        self.buttons_frame = ttk.Frame(self.master)
        self.buttons_frame.pack()
        self.reset_game()

        for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            button = ttk.Button(self.buttons_frame, text=letter.upper(), command=lambda l=letter: self.make_guess(l))
            button.grid(row=idx // 13, column=idx % 13)

        self.play_again_button = ttk.Button(self.master, text="Play Again", command=self.play_again)
        
    def reset_game(self):
        self.word = random.choice(self.keywords)
        self.word_completion = ["_"] * len(self.word)
        self.guessed_letters = []
        self.hangman_label["text"] = self.display_hangman()
        self.word_label["text"] = " ".join(self.word_completion)

    def make_guess(self, guessed_letter):
        if guessed_letter in self.guessed_letters:
            return
        self.guessed_letters.append(guessed_letter)

        if guessed_letter not in self.word:
            self.tries -= 1
        else:
            for i, letter in enumerate(self.word):
                if letter == guessed_letter:
                    self.word_completion[i] = guessed_letter

        self.hangman_label["text"] = self.display_hangman()
        self.word_label["text"] = " ".join(self.word_completion)

        if "_" not in self.word_completion or self.tries == 0:
            self.game_over()

    def game_over(self):
        self.play_again_button.pack(pady=20)

    def play_again(self):
        self.play_again_button.pack_forget()
        self.reset_game()

    def display_hangman(self):
        stages = [
            "Stage 1",
            "Stage 2",
            "Stage 3",
            "Stage 4",
            "Stage 5",
            "Stage 6",
            "Stage 7",
        ]
        return stages[self.tries] if self.tries < len(stages) else "Game Over"

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
