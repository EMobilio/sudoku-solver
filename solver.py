from board import *

def solve(board):
    return

""" Inputs: board- Board object
            value- integer from 0-9 to be checked
            row-  row index of the position to be checked
            col- column index of the position to be checked
            
    Outputs: a boolean indicating whether the given value can be placed in the specified 
    position on the board based on whether the value is already in the position's
    row, column or inner box
"""
def isValid(board, value, row, col):
    # check if the value is already in the row
    for c in range(len(board.cells[0])):
        if (board.cells[row][c] == value):
            return False
        
    # check if the value is already in the column
    for r in range(len(board.cells)):
        if (board.cells[r][col] == value):
            return False

    # check if the value is already in the inner 3x3 box the given position 
    # lies in (position (row, col) falls in the inner box in the range of 
    # rows from 3*(row // 3) to 3*(row // 3) + 3 - 1 and colums from 3*(col) // 3) to 
    # 3*(row // 3) + 3 - 1)
    for r in range(3*(row // 3) , 3*(row // 3) + 3):
        for c in range(3*(col // 3), 3*(col // 3) + 3):
            if (board.cells[r][c] == value):
                return False

    # if the value is not in the row, column or inner box, the position is valid
    return True

