from minesweeper import *

# initial_state = Minefield(4, 4, 3)
# minesweeper = Minesweeper(initial_state)
# heuristic = 3
# result = minesweeper.play_game(heuristic)

# final_state = result[0]
# win = result[1]
# moves = result[2]

# print(final_state)
# print(f"Win: {win}")
# print(f"Moves: {moves}")
# print()

wins = 0
for i in range(1000):
    initial_state = Minefield(4, 4, 3)
    minesweeper = Minesweeper(initial_state)
    heuristic = 1
    result = minesweeper.play_game(heuristic) 
    if result[1] == True:
        wins += 1
print(wins)   
