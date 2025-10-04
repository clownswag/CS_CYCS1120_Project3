import random
import string

class Boggle_Board:
    def __init__(self):
        self.board = [[' ' for _ in range(4)] for _ in range(4)]
        self.visited = [[False for _ in range(4)] for _ in range(4)]
    
    def fill_board(self, seed=None):
        if seed is not None:
            random.seed(seed)

        for row in range(4):
            for col in range(4):
                self.board[row][col] = random.choice(string.ascii_uppercase)
    
    def display_board(self, found_words=None):
        print("+---+---+---+---+")
        for row in range(4):
            print("|", end="")
            for col in range(4):
                letter = self.board[row][col]
                if found_words and letter in found_words:
                    print(f"<{letter}>", end="|")
                else:
                    print(f" {letter} ", end="|")
            print()
            print("+---+---+---+---+")