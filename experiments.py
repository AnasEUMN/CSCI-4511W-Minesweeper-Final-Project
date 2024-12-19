from minesweeper import *

def test_minesweeper_heuristic(heuristic, games, x, y, mines):
    wins = 0
    moves = 0
    for i in range(games):
        initial_state = Minefield(x, y, mines)
        minesweeper = Minesweeper(initial_state)
        result = minesweeper.play_game(heuristic) 
        print(result[0])
        if result[1]:
            wins += 1
        moves += result[2]
    print(f"Wins: {wins}/{games}") 
    print(f"Moves: {moves}") 

test_minesweeper_heuristic(5, 100, 6, 6, 6)
