class Board:
    """ A class for objects representing a 9x9 sudoku board """


    """ initializer for an empty 9x9 board with 0s representing blank spaces """
    def __init__(self):
        self.cells = [[0] * 9 for row in range(9)]

    """ method for representing the board object as a sring """
    def __repr__(self):
        s = ""

        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                if (col == len(self.cells[0]) - 1):
                    s += " " + str(self.cells[row][col]) + "\n"
                else:
                    s += " " + str(self.cells[row][col]) + " |"

            if (row != len(self.cells) - 1):
                for col in range(len(self.cells[0])):
                    if (col == len(self.cells[0]) - 1):
                        s += "---\n"
                    else:
                        s += "----"

        return s
    
    """ method that loops through the board's cells to create
        a list of all of the empty positions in the board
    """
    def getBlanks(self):
        blanks = []

        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                if self.cells[row][col] == 0:
                    blanks += [(row, col)]

        return blanks
    
