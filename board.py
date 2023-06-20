from dokusan import generators

class Board:
    """ A class for objects representing a 9x9 sudoku board """
    NUM_ROWS = 9
    NUM_COLS = 9

   
    def __init__(self, rank):
        """ Initializer that takes a rank representing the difficulty level
            and uses dokusan to generate a puzzle of the specified difficulty,
            copying the puzzle to the cells field. 0 represents an empty space
        """
        # initialize an empty 9x9 2-D list 
        self.cells = [[""] * self.NUM_ROWS for row in range(self.NUM_COLS)]
 
        # generate a puzzle string with dokusan
        puzzle = str(generators.random_sudoku(rank))

        # fill in self.cells with corresponding values in the puzzle string
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                self.cells[row][col] = int(puzzle[self.NUM_ROWS*row + col])

    def __repr__(self):
        """ method for representing the board object as a sring """
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
    
    def getBlank(self):
        """ loops through the board's cells to find and return tuple representing the 
            position of a blank space (or None if the board is complete)
        """
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if self.cells[row][col] == 0:
                    return (row, col)

        return None
    
    
    def placeValue(self, value, row, col):
        """ Inputs: value- integer from 1-9 to be placed
                row- row index
                col- column index
                
            updates self.cells by placing the specified value
            in the specified position indicated by row and col
        """
        self.cells[row][col] = value
        

    
    def removeValue(self, row, col):
        """ Inputs: row- row index of value to be removed
                col- column index of value to be removed
                
            updates self.cells by removing the value rom the specified position
            indicated by row and col by setting the value at the position to 0
        """
        self.cells[row][col] = 0

