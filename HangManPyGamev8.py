import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PapHigh Clean Water Game')
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 128, 255)

# Variables
keywords = ["plastic", "pollution", "ocean", "marine", "rahui", "microplastics", "recycle", "waste", "ecosystem", "tangaroa"]
word = random.choice(keywords)
word_completion = ['_'] * len(word)
guessed_letters = []
tries = 7
#Reset function to guess more than one word
'''def reset_game():
    global word, word_completion, guessed_letters, tries
    word = random.choice(keywords)
    word_completion = ['_'] * len(word)
    guessed_letters = []
    tries = 7'''
#Introduce the game with instructions
'''def show_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False

        SCREEN.fill(WHITE)
        text_surface = FONT.render("Welcome to Hangman!", True, BLACK)
        SCREEN.blit(text_surface, (300, 200))
        text_surface = FONT.render("Press SPACE to start", True, BLACK)
        SCREEN.blit(text_surface, (300, 300))
        pygame.display.update()'''


   
# Main loop
running = True
#show_intro()  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
                button_rect = pygame.Rect(50 + i * 30, 500, 20, 20)
                if button_rect.collidepoint(x, y):
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter not in word:
                            tries -= 1
                        else:
                            for idx, char in enumerate(word):
                                if char == letter:
                                    word_completion[idx] = letter
# Check for win or lose
    if '_' not in word_completion:
        text_surface = FONT.render("You win! Press 'R' to restart or 'Q' to quit.", True, BLACK)
        SCREEN.blit(text_surface, (50, 250))
        pygame.display.flip()
        waiting_for_action = True
        while waiting_for_action:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset_game()
                        waiting_for_action = False
                    elif event.key == pygame.K_q:
                        running = False
                        waiting_for_action = False
    elif tries == 0:
        text_surface = FONT.render(f"You lose! The word was {word}. Press 'R' to restart or 'Q' to quit.", True, BLACK)
        SCREEN.blit(text_surface, (50, 250))
        pygame.display.flip()
        waiting_for_action = True
        while waiting_for_action:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset_game()
                        waiting_for_action = False
                    elif event.key == pygame.K_q:
                        running = False
                        waiting_for_action = False
   # show_intro()

    # Draw everything
    SCREEN.fill(WHITE)

    # Draw word completion
    text_surface = FONT.render(' '.join(word_completion), True, BLACK)
    SCREEN.blit(text_surface, (50, 50))

    # Draw buttons
    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        button_rect = pygame.Rect(50 + i * 30, 500, 20, 20)
        pygame.draw.rect(SCREEN, BUTTON_COLOR, button_rect)
        text_surface = FONT.render(letter.upper(), True, BLACK)
        SCREEN.blit(text_surface, (55 + i * 30, 500))

    # Draw hangman (simplified)
    if tries < 7:
        pygame.draw.line(SCREEN, BLACK, (400, 100), (400, 200), 5)
    if tries < 6:
        pygame.draw.circle(SCREEN, BLACK, (400, 250), 50, 5)
    if tries < 5:
        pygame.draw.line(SCREEN, BLACK, (400, 300), (400, 400), 5)
    if tries < 4:
        pygame.draw.line(SCREEN, BLACK, (400, 300), (350, 350), 5)
    if tries < 3:
        pygame.draw.line(SCREEN, BLACK, (400, 300), (450, 350), 5)
    if tries < 2:
        pygame.draw.line(SCREEN, BLACK, (400, 400), (350, 450), 5)
    if tries < 1:
        pygame.draw.line(SCREEN, BLACK, (400, 400), (450, 450), 5)

    pygame.display.flip()

    # Check for win or lose
    if '_' not in word_completion:
        print("You win!")
        running = False
    elif tries == 0:
        print(f"You lose! The word was {word}")
        running = False

pygame.quit()
