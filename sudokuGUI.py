import pygame
import datetime
from sys import exit
from GUIboard import *

WIDTH, HEIGHT = 800, 700
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Difficulty constants
EASY = 50
MEDIUM = 150
HARD = 450

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
start_time = 0
final_time = 0

# Fonts
TITLE_FONT = pygame.font.SysFont("comicsans", 80)
BUTTON_FONT = pygame.font.SysFont("comicsans", 30)
WIN_FONT = pygame.font.SysFont("comicsans", 50)
TIMER_FONT = pygame.font.SysFont("comicsans", 40)

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

game_button = pygame.Rect(0, 0, 300, 100)
game_button.center = (WIDTH/2, 625)

solve_text = BUTTON_FONT.render("Solve For Me", False, BLACK)
return_text = BUTTON_FONT.render("Return Home", False, BLACK)
win_msg = WIN_FONT.render("Solved!", False, BLACK)

def draw_screen(game_active, solved, board, start_time):
    """ Input: game_active- boolean representing whether the game is active
               solved- boolean representing whether the puzzle has been solved 
               board- Board object
               start_time- integer representing the time in milliseconds since the game was started
    
        Draws the current state of the screen based on inputs
    """
    # if game is active or puzzle is solved draw the game board and screen, otherwise draw the title screen
    if game_active or solved:
        current_time = pygame.time.get_ticks() - start_time
        screen.fill(WHITE)
        board.draw_board(screen, solved)
        pygame.draw.rect(screen, BLUE, game_button, border_radius=20)
        if solved:
            time = str(datetime.timedelta(milliseconds=final_time))
            time_text = TIMER_FONT.render(time[:-4], False, BLACK)
            screen.blit(return_text, 
                        (game_button.x + game_button.width/2 - return_text.get_width()/2, game_button.y + game_button.height/2 - return_text.get_height()/2))
            screen.blit(win_msg, 
                        (WIDTH/2 - game_button.width/2 - 125 - win_msg.get_width()/2, game_button.y + game_button.height/2 - win_msg.get_height()/2))
        else:
            time = str(datetime.timedelta(milliseconds=current_time))
            time_text = TIMER_FONT.render(time[:-4], False, BLACK)
            screen.blit(solve_text, 
                        (game_button.x + game_button.width/2 - solve_text.get_width()/2, game_button.y + game_button.height/2 - solve_text.get_height()/2))
        screen.blit(time_text, 
                    (WIDTH/2 + game_button.width/2 + 25, game_button.y + game_button.height/2 - time_text.get_height()/2))
    else: 
        screen.fill(WHITE)
        screen.blit(title, (WIDTH/2 - title.get_width()/2, 60))
        pygame.draw.rect(screen, GREEN, easy_button, border_radius=20)
        screen.blit(easy_text, 
                    (easy_button.x + easy_button.width/2 - easy_text.get_width()/2, easy_button.y + easy_button.height/2 - easy_text.get_height()/2))
        pygame.draw.rect(screen, YELLOW, medium_button, border_radius=20)
        screen.blit(medium_text, 
                    (medium_button.x + medium_button.width/2 - medium_text.get_width()/2, medium_button.y + medium_button.height/2 - medium_text.get_height()/2))
        pygame.draw.rect(screen, RED, hard_button, border_radius=20)
        screen.blit(hard_text, 
                    (hard_button.x + hard_button.width/2 - hard_text.get_width()/2, hard_button.y + hard_button.height/2 - hard_text.get_height()/2))
    
    pygame.display.update()

def main():
    """ main game loop """
    run = True
    game_active = False
    solved = False
    board = None
    clicked = False
    global start_time
    global final_time

    while run:
        clock.tick(FPS)

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # check for clicks here to avoid continuous clicking
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

            if game_active == False and solved == False:
                # check for button presses
                if clicked:
                    if easy_button.collidepoint(event.pos):
                        start_time = pygame.time.get_ticks()
                        game_active = True
                        board = Board(EASY)
                    if medium_button.collidepoint(event.pos):
                        start_time = pygame.time.get_ticks()
                        game_active = True
                        board = Board(MEDIUM)
                    if hard_button.collidepoint(event.pos):
                        start_time = pygame.time.get_ticks()
                        game_active = True
                        board = Board(HARD)
                    clicked = False

            if game_active == True and solved == False:
                # check if the user has clicked a cell
                if clicked:
                    board.click(event.pos)
                    if game_button.collidepoint(event.pos):
                        board.clearBoard()
                        board.solve(game_active, solved, start_time)
                        solved = True
                    clicked = False

                # check if the user is entering or deleting a value
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        board.place(1)
                    if event.key == pygame.K_2:
                        board.place(2)
                    if event.key == pygame.K_3:
                        board.place(3)
                    if event.key == pygame.K_4:
                        board.place(4)
                    if event.key == pygame.K_5:
                        board.place(5)
                    if event.key == pygame.K_6:
                        board.place(6)
                    if event.key == pygame.K_7:
                        board.place(7)
                    if event.key == pygame.K_8:
                        board.place(8)
                    if event.key == pygame.K_9:
                        board.place(9)
                    if event.key == pygame.K_BACKSPACE:
                        board.delete()
                        
            if solved == True:
                # check for button presses
                if clicked:
                    if game_button.collidepoint(event.pos):
                        solved = False
                        game_active = False
                        board = None
                    clicked = False

        if game_active:
            solved = board.isSolved()
            if solved:
                final_time = pygame.time.get_ticks() - start_time
                game_active = False

        draw_screen(game_active, solved, board, start_time)

if __name__ == "__main__":
    main()