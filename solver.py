from board import *


def solve(board):
    """ Input: board- Board object

        A function using a recursive backtracking algorithm to solve a sudoku puzzle.
        Returns a boolean and prints the solved puzzle once it is found.
    """
    position = board.getBlank() # get the next empty postion in the board

    # if there are no more empty positions, the puzzle has been solved; print the solution
    if position == None:
        print("Solution found:")
        print()
        print(board)
        return True
    
    # loop through ints 1-9 and check if they are valid in the current empty position,
    # if yes place the value in the position and make a recursive call to fill the next
    # empty position
    for num in range(1, 10):
        if isValid(board, num, position[0], position[1]):
            board.placeValue(num, position[0], position[1])
            if solve(board) == True:
                return True
            board.removeValue(position[0], position[1])

    return False


def isValid(board, value, row, col):
    """ Inputs: board- Board object
            value- integer from 1-9 to be checked
            row-  row index of the position to be checked
            col- column index of the position to be checked
            
            Outputs: a boolean indicating whether the given value can be placed in the 
            specified position on the board based on whether the value is already in the 
            position's row, column or inner box
    """

    # check if the value is already in the row
    for c in range(len(board.cells[0])):
        if board.cells[row][c] == value:
            return False
        
    # check if the value is already in the column
    for r in range(len(board.cells)):
        if board.cells[r][col] == value:
            return False

    # check if the value is already in the inner 3x3 box the given position 
    # lies in (position (row, col) falls in the inner box in the range of 
    # rows from 3*(row // 3) to 3*(row // 3) + 3 - 1 and colums from 3*(col) // 3) to 
    # 3*(row // 3) + 3 - 1)
    for r in range(3*(row // 3) , 3*(row // 3) + 3):
        for c in range(3*(col // 3), 3*(col // 3) + 3):
            if board.cells[r][c] == value:
                return False

    # if the value is not in the row, column or inner box, the position is valid
    return True

def main():
    """ main program execution loop function """
    while True:
        try: 
            rank = int(input("Enter a rank from 1-1000 (low end is easy, high end is hard): "))
        except ValueError:
            print("Please enter an integer from 1-1000")
            continue
        if rank < 1 or rank > 1000:
            print("Please enter an integer from 1-1000")
            continue
        else:
            break
        
    board = Board(rank)
    print("Initial Board:")
    print()
    print(board)

    while True:
        try:
            response = str(input("Find solution? (y/n): "))
        except ValueError:
            print("Please respone 'y' or 'n'")
            continue
        if response == "y":
            solve(board)
            break
        elif response == "n":
            break
        else:
            print("Please respond with 'y' or 'n'")
            continue

main()