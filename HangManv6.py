from termcolor import colored
import random
import time


# Function to color ASCII art
def color_text(text, color):
    return colored(text, color)

# List of keywords related to plastic pollution in oceans
keywords = ["plastic", "pollution", "ocean", "marine", "rahui", "microplastics", "recycle", "waste", "ecosystem", "tangaroa"]

# ASCII Art for the game title
game_title = '''
  _   _                                         
 | | | |                                        
 | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  _  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 \\_| |_/\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/                       
'''

# Function to display the hangman graphic
def display_hangman(tries):
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
    return stages[7 - tries]

# Typewriter effect function
def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to play the hangman game
def play_hangman():
    word = random.choice(keywords)
    word_completion = "_" * len(word)  # Number of dashes matches the number of letters
    guessed = False
    guessed_letters = []
    tries = 7

    typewriter_effect("Let's play Hangman!")
    print(color_text(game_title, 'red'))
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Better luck next time!")

# Main function to start the game
def main():
    play_again = "yes"
    while play_again == "yes":
        play_hangman()
        play_again = input("Do you want to play again? (yes or no): ").lower()

if __name__ == "__main__":
    main()
