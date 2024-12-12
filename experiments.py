from minesweeper import *

initial_state = Minefield(5, 5, 4)
minesweeper = Minesweeper(initial_state)
heuristic = 1
result = minesweeper.play_game(heuristic)

final_state = result[0]
win = result[1]
moves = result[2]

print("--------------------")
print(final_state)
print(f"Win: {win}")
print(f"Moves: {moves}")
