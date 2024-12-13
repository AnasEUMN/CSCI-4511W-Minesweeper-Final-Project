from minesweeper import *

def test_minesweeper_heuristic(heuristic):
    wins = 0
    moves = 0
    for i in range(100):
        initial_state = Minefield(5, 5, 4)
        minesweeper = Minesweeper(initial_state)
        result = minesweeper.play_game(heuristic) 
        print(result[0])
        if result[1]:
            wins += 1
        moves += result[2]
    print(f"Wins: {wins}") 
    print(f"Moves: {moves}") 

test_minesweeper_heuristic(3)
