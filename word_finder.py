from board import BoggleBoard
from palindrome import IsPalindrome

class WordFinder:
    def __init__(self, boggle_board):
        self.boggle_board = boggle_board
        self.board = boggle_board.board
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

    def word_on_board(self, word):
        
        # Check if a word can be formed on the board. The method works by trying every starting cell
        # until it finds the first letter of the word, then it if found True it will call the recursive search_word method
        # to try and find the rest of the word. If the word is found, it returns True and the path taken to form the word.
        # If the word is not found, it returns False and an empty list.
        
        word = word.upper()

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == word[0]:
                    self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
                    path = []
                    if self.search_word(row, col, word, 0, path):
                        return True, path
        return False, []
    
    # This is a recursive method that we use to search for the word on the board in the function above.
    def search_word(self, row, col, word, index, path):
        if index == len(word):
            return True
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.visited[row][col] or self.board[row][col] != word[index]:
            return False
        self.visited[row][col] = True
        path.append((row, col))

        # The directions are how we can move on the board.
        directions = [
           #row #col
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]

        # Try all possible directions
        for rowchange, colchange in directions:
            if self.search_word(row + rowchange, col + colchange, word, index + 1, path):
                return True
            
        self.visited[row][col] = False
        path.pop()
        return False
    
    # This updates the board if the word is found
    def mark_board(self, word):
        found, path = self.word_on_board(word)
        if found:
            print('Nice Job!')
            checker = IsPalindrome(word)
            checker.is_palindrome()
            self.boggle_board.display_board(path)
            return True
        else:
            print("I don't see that word.")
            checker = IsPalindrome(word)
            checker.is_palindrome()
            print("Are we looking at the same board?")
    
