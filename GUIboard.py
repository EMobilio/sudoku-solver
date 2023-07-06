import pygame
from dokusan import generators

pygame.font.init()

class Board:
    """ A class for objects representing a 9x9 sudoku board """

    NUM_ROWS = 9
    NUM_COLS = 9

    def __init__(self, rank):
        """ Initializer that takes an integer (rank) representing the difficulty level
            and uses dokusan to generate a puzzle of the specified difficulty,
            copying the puzzle to the cells field, an array of Cell objects
        """
        self.cells = [[""] * self.NUM_COLS for row in range(self.NUM_ROWS)] # initialize empty 9x9 2D list
        self.selected = None # represents which cell has been selected by the player
        
        # generate a puzzle string with dokusan
        puzzle = str(generators.random_sudoku(rank))

        # loop through self.cells and create a Cell object corresponding to each space in the puzzle
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                digit = int(puzzle[self.NUM_ROWS*row + col])
                if digit != 0 :
                    self.cells[row][col] = Cell(digit, row, col, True)
                else:
                    self.cells[row][col] = Cell(None, row, col, False)

    def draw_board(self, screen):
        """ Input: screen- display surface

            Draws the grid lines of the board and calls the draw_cell() method
            for each cell
        """
        # draw grid lines
        for i in range(self.NUM_ROWS + 1):
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            pygame.draw.line(screen, (0, 0, 0), (130, 10 + i*60), (670, 10 + i*60), thickness)
            for j in range(self.NUM_COLS +1):
                if j % 3 == 0:
                    thickness = 3
                else:
                    thickness = 1
                pygame.draw.line(screen, (0, 0, 0), (130 + j*60, 10), (130 + j*60, 550), thickness)

        # draw cell values
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                self.cells[row][col].draw_cell(screen)
        
        
class Cell:
    """ A class for objects representing the individual cells of a sudoku board """
    
    USER_CELL_FONT = pygame.font.SysFont("arial", 30)
    GIVEN_CELL_FONT = pygame.font.SysFont("arial", 30, bold=True)

    def __init__(self, val, row, col, given):
        """ Initializer that takes integer (or None if empty) representing the value of the
            cell (val), integers representing the row and column index of the cell (row, col),
            and a boolean representing if the value of the cell is a given clue (given)
        """
        self.val = val
        self.row = row
        self.col = col
        self.given = given

    def draw_cell(self, screen):
        """ Input: screen- display surface
        
            Draws the cell value to the screen its proper location
        """
        # determine which text type to use based on if the cell value was given or input by the user
        if self.given == True:
            cell_text = self.GIVEN_CELL_FONT.render(str(self.val), False, (0, 0, 0))
        else:
            cell_text = self.USER_CELL_FONT.render(str(self.val), False, (0, 0, 0))

        # draw value if not None
        if self.val != None:
            screen.blit(cell_text, 
                        (130 + 60*self.col + 30 - cell_text.get_width()/2, 10 + 60*self.row + 30 - cell_text.get_height()/2))