# <p align=center>sudoku-solver</p>
<p align=center><img width="314" alt="Title" src="https://github.com/EMobilio/sudoku-solver/assets/109104115/b2a140c4-fa21-4c29-8f79-20c5f9990749"></p>

## About
A simple Sudoku application implemented using Python and Pygame. 

My goal was to create an interesting version of algorithm visualization, so I decided to implement Sudoku with a solving feature which would rely on a backtracking algorithm and allow the user to see how such an algorithm functions. I started by implementing the algorithm in a text-based version of the solver where you can generate a puzzle and then have the algorithm solve it and print the result. I then used Pygame to create a fully playable GUI version of the game which includes the solving feature that displays every step of the algorithm on the GUI.

Since the GUI solving feature displays each step of the algorithm, solving puzzles can take excessive lengths of time. In particular, it can take the solver feature up to a few hours to run to completion on medium and hard puzzles. For the purposes of this project this isn't really an issue, since the goal is merely to visualize the algorithm. However, if you would like to see it run to completion, it is recommended that you run it on an easy puzzle, which should only take a few seconds to a couple of minutes. Without all of the extra steps to update and display the state of the board, the algorithm itself can solve puzzles of any difficulty in under a second, as seen in the text-based version.

<p float=left align=middle><img align= middle alt="GUI Demo" src="https://github.com/EMobilio/sudoku-solver/assets/109104115/e5d1b80f-dc9f-40c9-b7f8-1e9314ab876d"> <img align=middle alt="Text Demo" src="https://github.com/EMobilio/sudoku-solver/assets/109104115/a6052d28-93f4-4b6d-88cd-ddeca22566a7"></p>

## How to Run
Before running, make sure you have Python installed.

Run the following to install dependencies:
```
pip install -r requirements.txt
```

### Text-based Version
Run the text-based version using
```
python solver.py
```

### GUI Version
Run the GUI version using
```
python sudokuGUI.py
```

## How to Use
### Text-based Version
For the text-based solver, simply follow the prompts.

### GUI Version
Select one of the three difficulty levels. Click on a non-given cell (the entries of which are __bolded__) to select it for editing. Selected cells are highlighted in red on the borders. Type a digit from 1-9 to input it in the selected cell. Press 'delete' to clear an entry from a selected cell. Click the __'Solve For Me'__ button to run and visualize the backtracking solver algorithm.

## Future Scope
Future improvements might include:
- implementing a puzzle generator of my own
- implementing a pencil marking feature to imrpove the gameplay aspect
