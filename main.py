from board import BoggleBoard
from palindrome import IsPalindrome
from word_finder import WordFinder

def main():
    boggle = BoggleBoard()
    seed_input = input("Enter a seed value (or press Enter to skip): ")
    seed = int(seed_input) if seed_input.isdigit() else None
    boggle.fill_board(seed)
    boggle.display_board()

    finder = WordFinder(boggle)
    word = input("\nEnter word (in UPPERcase): ")
    finder.mark_board(word)


if __name__ == "__main__":
    main()