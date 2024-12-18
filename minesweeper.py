from minefield import *
import math
import random

def random_move(state):
    unrevealed = state.get_unrevealed_cells()
    index = random.randint(0, len(unrevealed) - 1)
    cell = unrevealed[index]
    return f"{cell.x},{cell.y}"

def neighbor_sum(state):
    revealed = state.get_revealed_cells()
    unrevealed_neighbors = []
    for cell in revealed:
        neighbors = state.get_neighborhood(cell.x,cell.y)
        for neighbor in neighbors:
            if not neighbor.revealed and neighbor not in unrevealed_neighbors:
                unrevealed_neighbors.append(neighbor)
    currCell = None
    currMin  = float('inf')
    for cell in unrevealed_neighbors:
        neighborhood = state.get_neighborhood(cell.x,cell.y)
        sum = 0
        for neighborCell in neighborhood:
            if neighborCell.revealed:
                sum += int(neighborCell.status)
        if sum < currMin:
            currMin = sum
            currCell = cell
    return f"{currCell.x},{currCell.y}"


def minimize_mine_probability(state):
    probabilities = []
    S = state.get_S()
    unrevealed = state.get_unrevealed_cells()
    for cell in unrevealed:
        numerator = []
        for s in S:
            if cell in s:
                numerator.append(s)
        probabilities.append((cell, len(numerator) / len(S)))
    best = (probabilities[0][0], probabilities[0][1])
    for cell, probability in probabilities:
        if probability < best[1]:
            best = (cell, probability)
    bests = []
    for cell, probability in probabilities:
        if probability == best[1]:
            bests.append((cell, probability))
    index = random.randint(0, len(bests) - 1)
    best = bests[index]
    best_move = f"{best[0].x},{best[0].y}"
    return best_move

def maximize_f_entropy(state):
    q_bs = []
    C = set(state.get_unrevealed_cells())
    S = set(tuple(s) for s in state.get_S())
    for i in range(len(state.field)):
        for j in range(len(state.field[0])):
            b = state.field[i][j]
            if b in C:
                U_b = set(state.get_neighborhood(b.x, b.y))
                q_b = 0
                for n in range(len(U_b) + state.mines): 
                    S_b_n = []
                    for s in S:
                        s = set(s)
                        if (b not in s) and (n == len(U_b & s)):
                            S_b_n.append(tuple(s))
                    p_b_n = len(S_b_n) / len(S)
                    if p_b_n > 0:
                        q_b -= (p_b_n * math.log2(p_b_n))
                q_bs.append((b, q_b))
    best = (q_bs[0][0], q_bs[0][1])
    for b, q_b in q_bs:
        if q_b > best[1]:
            best = (b, q_b)
    bests = []
    for b, q_b in q_bs:
        if q_b == best[1]:
            bests.append((b, q_b))
    index = random.randint(0, len(bests) - 1)
    best = bests[index]
    best_move = f"{best[0].x},{best[0].y}"
    return best_move

def combine_min_probability_max_entropy(state):
    probabilities = []
    S = state.get_S()
    unrevealed = state.get_unrevealed_cells()
    for cell in unrevealed:
        numerator = []
        for s in S:
            if cell in s:
                numerator.append(s)
        probabilities.append((cell, len(numerator) / len(S)))
    best_p = (probabilities[0][0], probabilities[0][1])
    for cell, probability in probabilities:
        if probability < best_p[1]:
            best_p = (cell, probability)
    best_ps = []
    for cell, probability in probabilities:
        if probability == best_p[1]:
            best_ps.append(cell)
    q_bs = []
    for i in range(len(state.field)):
        for j in range(len(state.field[0])):
            b = state.field[i][j]
            if b in best_ps:
                U_b = set(state.get_neighborhood(b.x, b.y))
                q_b = 0
                for n in range(len(U_b) + state.mines): 
                    S_b_n = []
                    for s in S:
                        s = set(s)
                        if (b not in s) and (n == len(U_b & s)):
                            S_b_n.append(tuple(s))
                    p_b_n = len(S_b_n) / len(S)
                    if p_b_n > 0:
                        q_b -= (p_b_n * math.log2(p_b_n))
                q_bs.append((b, q_b))
    best = (q_bs[0][0], q_bs[0][1])
    for b, q_b in q_bs:
        if q_b > best[1]:
            best = (b, q_b)
    bests = []
    for b, q_b in q_bs:
        if q_b == best[1]:
            bests.append((b, q_b))
    index = random.randint(0, len(bests) - 1)
    best = bests[index]
    best_move = f"{best[0].x},{best[0].y}"
    return best_move

class Minesweeper():
    def __init__(self, initial):
        """ Define initial state """
        self.state = initial
    
    def best_action(self, heuristic):
        """ Given a Minesweeper state, return the best action according to the given Minesweeper heuristic """
        if heuristic == 1:
            best_action = random_move(self.state)
        elif heuristic == 2:
            best_action = neighbor_sum(self.state)
        elif heuristic == 3:
            best_action = minimize_mine_probability(self.state)
        elif heuristic == 4:
            best_action = maximize_f_entropy(self.state)
        elif heuristic == 5:
            best_action = combine_min_probability_max_entropy(self.state)
        return best_action 

    def goal_test(self):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return self.state.game_over()
    
    def play_game(self, heuristic):
        """ Game loop for Minesweeper. This uses a heuristic to test which cell to reveal before taking actions.
        In Minesweeper, once an action is taken, there is no going back. """
        win = False
        moves = 0
        while not self.goal_test():
            print(self.state)
            action = self.best_action(heuristic)
            cell = action.split(",")
            win = self.state.reveal_cell(int(cell[0]), int(cell[1]), False)
            moves += 1
        return (self.state, win, moves)   
    