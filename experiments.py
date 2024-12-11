from minesweeper import *

initial_state = Minefield(16, 16, 40)
minesweeper = Minesweeper(initial_state)
heuristic = 1
(final_state, win, moves) = minesweeper.play_game(heuristic)
