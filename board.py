import random
import string

class BoggleBoard:
    def __init__(self):
# Initialize a 4x4 board and a visited matrix
        self.board = [[' ' for _ in range(4)] for _ in range(4)]
        self.visited = [[False for _ in range(4)] for _ in range(4)]
    
    def fill_board(self, seed=None):
# Fill the board with random uppercase letters. If a seed is provided, use it for reproducibility.
        if seed is not None:
            random.seed(seed)

        for row in range(4):
            for col in range(4):
                self.board[row][col] = random.choice(string.ascii_uppercase)
    
    def display_board(self, path=None):
# Display the board in a readable format. If a path is provided, highlight the letters in the path.
        print("+---+ +---+ +---+ +---+")
        for row in range(4):
            for col in range(4):
                letter = self.board[row][col]
                if path and (row, col) in path:
                    print(f"|<{letter}>|", end=" ")
                else:
                    print(f"| {letter} |", end=" ")
            print()
            print("+---+ +---+ +---+ +---+")
