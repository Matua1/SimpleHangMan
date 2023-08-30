from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys
import random

class HangmanApp(QWidget):
    def __init__(self):
        super().__init__()

        self.keywords = ["plastic", "pollution", "ocean", "marine", "rahui", "microplastics", "recycle", "waste", "ecosystem", "tangaroa"]
        self.word = random.choice(self.keywords)
        self.word_completion = ['_'] * len(self.word)
        self.tries = 7

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.hangman_label = QLabel(self.display_hangman())
        vbox.addWidget(self.hangman_label)

        self.word_label = QLabel(' '.join(self.word_completion))
        vbox.addWidget(self.word_label)

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            btn = QPushButton(letter.upper())
            btn.clicked.connect(self.make_guess)
            vbox.addWidget(btn)

        self.setLayout(vbox)
        self.setWindowTitle('Hangman Game')
        self.show()

    def make_guess(self):
        sender = self.sender()
        guessed_letter = sender.text().lower()

        if guessed_letter in self.word:
            for i, letter in enumerate(self.word):
                if letter == guessed_letter:
                    self.word_completion[i] = guessed_letter
            self.word_label.setText(' '.join(self.word_completion))
        else:
            self.tries -= 1
            self.hangman_label.setText(self.display_hangman())

        if '_' not in self.word_completion:
            self.word_label.setText("You win!")
        elif self.tries == 0:
            self.word_label.setText(f"You lose! The word was {self.word}")

    # Function to display the hangman graphic
    def display_hangman(tries):
        stages = [
        
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
#    return stages[7.tries]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HangmanApp()
    sys.exit(app.exec_())
