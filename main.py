from board import Boggle_Board

def main():
    boggle = Boggle_Board()
    seed_input = input("Enter a seed value (or press Enter to skip): ")
    seed = int(seed_input) if seed_input.isdigit() else None
    boggle.fill_board(seed)
    boggle.display_board()

if __name__ == "__main__":
    main()