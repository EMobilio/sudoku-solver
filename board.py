from dokusan import generators

class Board:
    """ A class for objects representing a 9x9 sudoku board """
    NUM_ROWS = 9
    NUM_COLS = 9

    """ Initializer that takes a rank representing the difficulty level
        and uses dokusan to generate a puzzle of the specified difficulty,
        copying the puzzle to the cells field. 0 represents an empty space
    """
    def __init__(self, rank):
        # initialize an empty 9x9 2-D list 
        self.cells = [[""] * self.NUM_ROWS for row in range(self.NUM_COLS)]
 
        # generate a puzzle string with dokusan
        puzzle = str(generators.random_sudoku(rank))

        # fill in self.cells with corresponding values in the puzzle string
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                self.cells[row][col] = int(puzzle[self.NUM_ROWS*row + col])

    """ method for representing the board object as a sring """
    def __repr__(self):
        s = ""

        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if (col == self.NUM_COLS - 1):
                    s += " " + str(self.cells[row][col]) + "\n"
                else:
                    s += " " + str(self.cells[row][col]) + " |"

            if (row != self.NUM_ROWS - 1):
                for col in range(self.NUM_COLS):
                    if (col == self.NUM_COLS - 1):
                        s += "---\n"
                    else:
                        s += "----"

        return s
    
    """ method that loops through the board's cells to find and return
        a tuple representing the position of a blank space (or None if
        the board is complete)
    """
    def getBlank(self):
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if self.cells[row][col] == 0:
                    return (row, col)

        return None

