from search import *

initial_state = Minefield(16, 16, 40)

(final_state, win, moves) = minesweeper_astar_search(initial_state, 1)
