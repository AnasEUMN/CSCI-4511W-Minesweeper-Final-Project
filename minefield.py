import random

class Cell:
    def __init__(self, revealed, status):
        self.revealed = revealed
        self.status = status    

class Minefield:
    def __init__(self, rows, cols, mines):
        # Minefield size is not expected to be very large
        self.flags = mines
        self.field = []
        for i in range(rows):
            row = []
            for j in range(cols):
                cell = Cell(False, "-")
                row.append(cell)
            self.field.append(row)
        self.place_mines(0, 0, mines)
        self.evaluate_field()
        # Always reveals the top left corner first
        self.reveal_start_area(0, 0)

    def place_mines(self, x, y, mines):
        while mines > 0:
            xRandom = -1
            yRandom = -1
            success = False
            while not success:
                xRandom = random.randint(0, len(self.field) - 1)
                yRandom = random.randint(0, len(self.field[0]) - 1)
                success = True
                if xRandom == x and yRandom == y:
                    # Avoids placing a mine at the given coordinate
                    success = False 
                if self.field[xRandom][yRandom].status == "M":
                    # Avoids placing a mine in a cell that already has a mine
                    success = False
                if self.field[xRandom][yRandom].revealed:
                    # Avoids placing a mine in a revealed cell
                    success = False
            self.field[xRandom][yRandom].status = "M"
            mines -= 1

    def evaluate_field(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].status == "-":
                    self.field[i][j].status = "0"
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].status == "M":
                    # Increments surrounding cells if a mine is found
                    if i - 1 >= 0:
                        if self.field[i - 1][j].status != "M":
                            self.field[i - 1][j].status = str(int(self.field[i - 1][j].status) + 1)
                    if i + 1 < len(self.field):
                        if self.field[i + 1][j].status != "M":
                            self.field[i + 1][j].status = str(int(self.field[i + 1][j].status) + 1)
                    if j - 1 >= 0:
                        if self.field[i][j - 1].status != "M":
                            self.field[i][j - 1].status = str(int(self.field[i][j - 1].status) + 1)
                    if j + 1 < len(self.field[0]):
                        if self.field[i][j + 1].status != "M":
                            self.field[i][j + 1].status = str(int(self.field[i][j + 1].status) + 1)
                    if i - 1 >= 0 and j - 1 >= 0:
                        if self.field[i - 1][j - 1].status != "M":
                            self.field[i - 1][j - 1].status = str(int(self.field[i - 1][j - 1].status) + 1)
                    if i - 1 >= 0 and j + 1 < len(self.field[0]):
                        if self.field[i - 1][j + 1].status != "M":
                            self.field[i - 1][j + 1].status = str(int(self.field[i - 1][j + 1].status) + 1)
                    if i + 1 < len(self.field) and j - 1 >= 0:
                        if self.field[i + 1][j - 1].status != "M":
                            self.field[i + 1][j - 1].status = str(int(self.field[i + 1][j - 1].status) + 1)
                    if i + 1 < len(self.field) and j + 1 < len(self.field[0]):
                        if self.field[i + 1][j + 1].status != "M":
                            self.field[i + 1][j + 1].status = str(int(self.field[i + 1][j + 1].status) + 1)

    def reveal_zeroes(self, x, y):
        stack = []
        start = [x, y]
        stack.append(start)
        while len(stack) > 0:
            top = stack.pop()
            row = top[0]
            col = top[1]
            self.field[row][col].revealed = True
            if row - 1 >= 0:
                if self.field[row - 1][col].status == "0" and not self.field[row - 1][col].revealed:
                    next = [row - 1, col]
                    stack.append(next)
            if row + 1 < len(self.field):
                if self.field[row + 1][col].status == "0" and not self.field[row + 1][col].revealed:
                    next = [row + 1, col]
                    stack.append(next) 
            if col - 1 >= 0:
                if self.field[row][col - 1].status == "0" and not self.field[row][col - 1].revealed:
                    next = [row, col - 1]
                    stack.append(next) 
            if col + 1 < len(self.field[0]):
                if self.field[row][col + 1].status == "0" and not self.field[row][col + 1].revealed:
                    next = [row, col + 1]
                    stack.append(next)   
        
    def reveal_start_area(self, x, y):
        queue = []
        start = [x, y]
        queue.append(start)
        while len(queue) > 0:
            removed = queue.pop(0)
            row = removed[0]
            col = removed[1]
            if self.field[row][col].status == "M":
                # Keeps revealing cells until a mine is revealed
                break 
            self.field[row][col].revealed = True
            if row - 1 >= 0 and not self.field[row - 1][col].revealed: 
                next = [row - 1, col]
                queue.append(next)
            if row + 1 < len(self.field) and not self.field[row + 1][col].revealed: 
                next = [row + 1, col]
                queue.append(next)
            if col - 1 >= 0 and not self.field[row][col - 1].revealed:
                next = [row, col - 1]
                queue.append(next)
            if col + 1 < len(self.field[0]) and not self.field[row][col + 1].revealed: 
                next = [row, col + 1]
                queue.append(next)

    def reveal_cell(self, x, y, flag):
        if flag:
            if self.flags > 0:
                self.field[x][y].status = "F"
                self.field[x][y].revealed = True
                return False
        else:
            if self.field[x][y].status == "0":
                self.field[x][y].revealed = True
                self.reveal_zeroes(x, y)
                return False
            elif self.field[x][y].status == "M":
                # Returns True if a mine was revealed
                self.field[x][y].revealed = True
                return True
        self.field[x][y].revealed = True
        return False

    def game_over(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].status == "M" and self.field[i][j].revealed:
                    return True
        all_revealed = True
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].status != "M" and not self.field[i][j].revealed:
                    all_revealed = False
                    break
        if all_revealed == True:
            return True
        return False
    
    def get_neighborhood(self, x, y):  # U(b)
        neighborhood = []
        if x - 1 >= 0:
            neighborhood.append(self.field[x - 1][y])
            if y - 1 >= 0:
                neighborhood.append(self.field[x - 1][y - 1])
            if y + 1 < len(self.field[0]):
                neighborhood.append(self.field[x - 1][y + 1])
        if x + 1 < len(self.field):
            neighborhood.append(self.field[x + 1][y]) 
            if y - 1 >= 0:
                neighborhood.append(self.field[x + 1][y - 1])
            if y + 1 < len(self.field[0]):
                neighborhood.append(self.field[x + 1][y + 1])
        if y - 1 >= 0:
            neighborhood.append(self.field[x][y - 1]) 
        if y + 1 < len(self.field[0]):
            neighborhood.append(self.field[x][y + 1]) 
        return neighborhood

    def get_mine_cells(self):  # M
        mines = []
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].status == "M":
                    mines.append(self.field[i][j])
        return mines 

    def get_num_neighboring_mines(self, x, y):  # f(b)
        count = 0
        if self.field[x][y].status != "M":
            count = int(self.field[x][y].status) 
        else:
            neighborhood = self.get_neighborhood(x, y)
            for cell in neighborhood:
                if cell.status == "M":
                    count += 1
        return count
    
    def get_revealed_cells(self):  # B
        revealed = []
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].revealed:
                    revealed.append(self.field[i][j])
        return revealed    
    
    def get_unrevealed_cells(self):  # C
        unrevealed = []
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if not self.field[i][j].revealed:
                    unrevealed.append(self.field[i][j])
        return unrevealed

    def __str__(self):
        board = "    "  
        for i in range(len(self.field[0])):
            board += f" {i:2}"
        board += "\n"
        board += "    ,"
        for i in range(len(self.field[0])):
            board += "---"  
        board += "\n"
        for i in range(len(self.field)):
            board += f"{i:2} |"  
            for j in range(len(self.field[0])):
                if self.field[i][j].revealed: 
                    board += f"  {self.field[i][j].status}"  
                else:
                    board += "  -" 
            board += "\n"
        return board
    
# m = Minefield(16, 16, 40)
# print(m)
       