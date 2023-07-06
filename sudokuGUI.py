import pygame
from sys import exit
from GUIboard import *

WIDTH, HEIGHT = 800, 700
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Difficulty constants
EASY = 100
MEDIUM = 500
HARD = 1000

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

# Fonts
TITLE_FONT = pygame.font.SysFont("comicsans", 80)
BUTTON_FONT = pygame.font.SysFont("comicsans", 30)

# Title text
title = TITLE_FONT.render("Sudoku", False, BLACK)

# Buttons
easy_text = BUTTON_FONT.render("Easy", False, BLACK)
easy_button = pygame.Rect(0, 0, 200, 100)
easy_button.center = (WIDTH/2, 300)

medium_text = BUTTON_FONT.render("Medium", False, BLACK)
medium_button = pygame.Rect(0, 0, 200, 100)
medium_button.center = (WIDTH/2, 420)

hard_text = BUTTON_FONT.render("Hard", False, BLACK)
hard_button = pygame.Rect(0, 0, 200, 100)
hard_button.center = (WIDTH/2, 540)

def draw_screen(game_active, board):
    """ Input: game_active- boolean representing whether the game is active
               board- Board object
    
        Draws the current state of the screen based on inputs
    """
    # if game is active draw the game board and screen, otherwise draw the title screen
    if game_active:
        screen.fill(WHITE)
        board.draw_board(screen)
    else: 
        screen.fill(WHITE)
        screen.blit(title, (WIDTH/2 - title.get_width()/2, 60))
        pygame.draw.rect(screen, GREEN, easy_button, border_radius=20)
        screen.blit(easy_text, 
                    (easy_button.x + easy_button.width/2 - easy_text.get_width()/2, easy_button.y + easy_button.height/2 - easy_text.get_height()/2,))
        pygame.draw.rect(screen, YELLOW, medium_button, border_radius=20)
        screen.blit(medium_text, 
                    (medium_button.x + medium_button.width/2 - medium_text.get_width()/2, medium_button.y + medium_button.height/2 - medium_text.get_height()/2,))
        pygame.draw.rect(screen, RED, hard_button, border_radius=20)
        screen.blit(hard_text, 
                    (hard_button.x + hard_button.width/2 - hard_text.get_width()/2, hard_button.y + hard_button.height/2 - hard_text.get_height()/2,))
    
    pygame.display.update()

def main():
    """ main game loop """
    run = True
    game_active = False
    board = None

    while run:
        clock.tick(FPS)

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active == False:
                # check for button presses
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        game_active = True
                        board = Board(EASY)
                    if medium_button.collidepoint(event.pos):
                        game_active = True
                        board = Board(MEDIUM)
                    if hard_button.collidepoint(event.pos):
                        game_active = True
                        board = Board(HARD)

        draw_screen(game_active, board)

if __name__ == "__main__":
    main()