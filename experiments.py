from minesweeper import *

def test_minesweeper_heuristic(heuristic):
    wins = 0
    for i in range(1000):
        initial_state = Minefield(4, 4, 3)
        minesweeper = Minesweeper(initial_state)
        result = minesweeper.play_game(heuristic) 
        print(result[0])
        if result[1]:
            wins += 1
    print(f"Wins: {wins}")  

test_minesweeper_heuristic(4)
