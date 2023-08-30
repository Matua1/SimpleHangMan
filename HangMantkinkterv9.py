import tkinter as tk
from tkinter import ttk
import random

class HangManApp:
  def __init__(self, master):
    self.master = master
    self.master.title("PapHigh CleanWater Game")
    self.master.geometry("600x400")

    self.hangman_label = ttk.Label(self.master)
    self.hangman_label.pack()

    self.word_label = ttk.Label(self.master)
    self.word_label.pack()

    self.buttons_frame = ttk.Frame(self.master)
    self.buttons_frame.pack()

    for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        button = ttk.Button(self.buttons_frame, text=letter.upper(), command=lambda l=letter: self.make_guess(l))
        button.grid(row=idx // 13, column=idx % 13)

    # Add a Play Again button (initially hidden)
#    self.play_again_button = ttk.Button(self.master, text="Play Again", command=self.play_again)

#    self.reset_game()  # Now it's safe to call reset_game
       

    def create_buttons(self):
        for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
            button = ttk.Button(self.buttons_frame, text=letter.upper(), command=lambda l=letter: self.make_guess(l))
            button.grid(row=idx // 13, column=idx % 13)
 #          self.play_again_button = ttk.Button(self.master, text="Play Again", command=self.play_again)

    def reset_game(self):
        self.word = random.choice(self.keywords)
        self.word_completion = ["_"] * len(self.word)
        self.guessed_letters = []
        self.tries = 7

        self.hangman_label["text"] = self.display_hangman()
        self.word_label["text"] = " ".join(self.word_completion)
        self.play_again_button.pack_forget()
        self.create_buttons()

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

        if "_" not in self.word_completion:
            self.word_label["text"] = "You win!"
        elif self.tries == 0:
            self.word_label["text"] = f"You lose! The word was {self.word}"

    def display_hangman(self):
        stages = [
            '''
           ------
           |   
           |   
           |   
           |   
           |   
           -
        ''',
        '''
           ------
           |    |
           |    
           |
           |
           |
           -
        ''',
        
        '''
           ------
           |    |
           |    😵
           |   
           |    
           |
           -
        ''',
        '''
           ------
           |    |
           |    😵
           |    |
           |    |
           |    
           -
        ''',
        '''
           ------
           |    |
           |    😵
           |   \|
           |    |
           |    
           -
        ''',
        '''
           ------
           |    |
           |    😵
           |   \|/
           |    |
           |    
           -
        ''',
        '''
           ------
           |    |
           |    😵
           |   \|/
           |    |
           |   / 
           -
        ''',
        '''
           ------
           |    |
           |    😵
           |   \|/
           |    |
           |   / \
           -
        ''',
        ]
        return stages[self.tries] if self.tries < len(stages) else "Game Over"

if __name__ == "__main__":
    root = tk.Tk()
    app = HangManApp(root)
    root.mainloop()


    
