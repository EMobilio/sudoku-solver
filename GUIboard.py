import pygame
from dokusan import generators

pygame.font.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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

    def draw_board(self, screen, solved):
        """ Input: screen- display surface
                   solved- boolean representing whether the puzzle has been solved

            Draws the grid lines of the board and calls the draw_cell() method
            for each cell
        """
        # draw grid lines
        for i in range(self.NUM_ROWS + 1):
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            pygame.draw.line(screen, BLACK, (130, 10 + i*60), (670, 10 + i*60), thickness)
            for j in range(self.NUM_COLS +1):
                if j % 3 == 0:
                    thickness = 3
                else:
                    thickness = 1
                pygame.draw.line(screen, BLACK, (130 + j*60, 10), (130 + j*60, 550), thickness)

        # draw cell values
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                self.cells[row][col].draw_cell(screen, self, solved)

    def click(self, pos):
        """ Input: pos- tuple of coordinates

            Determines if the user has clicked on a cell, converting the click
            position to an index on the board and calling the select() method
            if the selected cell was not a given clue
        """
        if 130 < pos[0] < 670 and 10 < pos[1] < 550:
            row = (pos[1] - 10)//60
            col = (pos[0] - 130)//60
            if self.cells[row][col].given == False:
                self.select(row, col)
    
    def select(self, row, col):
        """ Inputs: row- row index
                    col- column index

            Sets the boards selected attribute to the row and column index and
            sets the corresponding Cell objects selected attribute to True
        """
        self.selected = (row, col)
        # reset all cells' selected attributes to False and then set the newly selected one to True
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COLS):
                self.cells[i][j].selected = False
        self.cells[row][col].selected = True

    def place(self, val):
        """ Input: val- integer
        
            Sets the selected cell's val attribute to val
        """
        if self.selected != None:
            row = self.selected[0]
            col = self.selected[1]
            self.cells[row][col].val = val

    def delete(self):
        """ Sets the selected cell's val attribute to None """
        if self.selected != None:
            row = self.selected[0]
            col = self.selected[1]
            self.cells[row][col].val = None

    def isValid(self, val, row, col):
        """ Inputs: val- integer
                    row- row index (int)
                    col- column index (int)
          
            Outputs: a boolean indicating whether the given value can be placed in the 
            specified position on the board based on whether the value is already in the 
            position's row, column or inner box      
        """
        # check if the value is already in the row
        for c in range(self.NUM_COLS):
            if self.cells[row][c].val == val and c != col:
                return False
            
        # check if the value is already in the column
        for r in range(self.NUM_ROWS):
            if self.cells[r][col].val == val and r != row:
                return False

        # check if the value is already in the inner 3x3 box the given position 
        # lies in (position (row, col) falls in the inner box in the range of 
        # rows from 3*(row // 3) to 3*(row // 3) + 3 - 1 and colums from 3*(col) // 3) to 
        # 3*(row // 3) + 3 - 1) 
        for r in range(3*(row // 3) , 3*(row // 3) + 3):
            for c in range(3*(col // 3), 3*(col // 3) + 3):
                if self.cells[r][c].val == val and r != row and c != col:
                    return False

        # if the value is not in the row, column or inner box, the position is valid    
        return True
    
    def isSolved(self):
        """ Checks if the puzzle has been solved in its current state """
        # if any cell is empty or has an invalid value, return False
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if self.cells[row][col].val == None:
                    return False
                elif self.isValid(self.cells[row][col].val, row, col) == False:
                    return False
        
        # otherwise return True
        return True

        
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
        self.selected = False

    def draw_cell(self, screen, board, solved):
        """ Input: screen- display surface
                   board- Board object
                   solved- boolean representing if the puzzle has been solved
        
            Draws the cell value to the screen its proper location
        """
        # determine which text type to use based on if the cell value was given or input by the user
        if self.given == True:
            cell_text = self.GIVEN_CELL_FONT.render(str(self.val), False, BLACK)
        else:
            cell_text = self.USER_CELL_FONT.render(str(self.val), False, BLACK)

        # draw value if not None
        if self.val != None:
            screen.blit(cell_text, 
                        (130 + 60*self.col + 30 - cell_text.get_width()/2, 10 + 60*self.row + 30 - cell_text.get_height()/2))
            # if the value is not valid in the space, draw a red circle indicator
            if board.isValid(self.val, self.row, self.col) == False:
                pygame.draw.circle(screen, 
                                   RED, 
                                   (130 + 60*self.col + 30 - cell_text.get_width()/2 - 5, 10 + 60*self.row + 30 - cell_text.get_height()/2),
                                   5)
            
        # if the cell has been selected and the puzzle has not been solved draw a red rectangle around it
        if self.selected == True and not solved:
            pygame.draw.rect(screen, RED, (130 + self.col*60, 10 + self.row*60, 61, 61), width=3)
