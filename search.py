from minefield import *

def heuristic_1(state): 
    return "0,0"

def heuristic_2(state): 
    return "0,0"

def heuristic_3(state):
    return "0,0"

def heuristic_4(state):
    # Combine heuristics?
    return "0,0" 

class Minesweeper():
    def __init__(self, initial):
        """ Define initial state """
        self.state = initial
    
    def best_action(self, heuristic):
        """ Given a Minesweeper state, return the best action according to the given Minesweeper heuristic """
        if heuristic == 1:
            best_action = heuristic_1(self.state)
        elif heuristic == 2:
            best_action = heuristic_2(self.state)
        elif heuristic == 3:
            best_action = heuristic_3(self.state)
        elif heuristic == 4:
            best_action = heuristic_4(self.state)
        return best_action 

    def goal_test(self):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return self.state.game_over()
    
    def play_game(self, heuristic):
        """ Game loop search specific for a Minesweeper problem. This uses a heuristic to test which cell to reveal before taking actions.
        In Minesweeper, once an action is taken, there is no going back. """
        moves = 0
        while not self.goal_test(self.state):
            action = self.best_action(self.state, heuristic)
            cell = action.split(",")
            win = self.state.reveal_cell(int(cell[0]), int(cell[1]), False)
            moves += 1
        return (self.state, win, moves)   
    