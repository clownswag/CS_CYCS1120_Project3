# CS/CYCS1120 (Python) - Fall 2025
## Programming Project #3
**Tuesday Labs**

-   **Points**: 200
-   **Due Date**: 10/7/25 @ 11:59pm (Two-week Project)

---

### Project Objectives
* Using recursion to solve a problem
* Manipulating two-dimensional lists
* Reviewing OOP

### Project Overview
Boggle is a word game designed by Allan Turoff and trademarked by Parker Brothers, a division of Hasbro. The game is played using a plastic grid of lettered dice, in which players attempt to find words in sequences of adjacent letters.

The game begins by shaking a covered tray of sixteen cubic dice, each with a different letter printed on each of its sides. The dice settle into a 4x4 tray so that only the top letter of each cube is visible:

```

+---+ +---+ +---+ +---+
| L | | S | |<Y>| | U |
+---+ +---+ +---+ +---+
| P | | R | |<A>| | U |
+---+ +---+ +---+ +---+
| A | | K | |<W>| | V |
+---+ +---+ +---+ +---+
| L | | N | |<A>| | P |
+---+ +---+ +---+ +---+

````

For your program, assume that each die has 26 sides - each representing a different capital letter from the English alphabet. Players search for words that can be constructed from the letters of sequentially adjacent cubes, where "adjacent" cubes are those horizontally or vertically neighboring (the real game also allows diagonals, but you do not need to for this assignment). Each letter of the word is a neighbor of the previous letter and players may not use the same letter cube more than once per word.

For example, in the above configuration of letters, the following words (and possibly more) can be found:
* AWAY
* RAW

---

### Project Structure
Write a program that runs a game of Boggle for a single player. Your program must perform the following tasks:
* Ask the player to enter a seed for randomizing the letters.
    * A seed is useful for testing, because each run will generate the same letters.
    * The sample board above was generated using 9999 for the seed.
* Generate a random 4x4 board of letters.
* Display the board.
* Allow the player to guess a word and then verify its validity on the board.
    * Valid words start at any position, and then each subsequent letter of the word is a neighbor of the previous letter.
    * You only need to consider horizontal and vertical neighbors (NOT diagonal).
* Indicate to the player whether or not the word is valid, and if so, print the board again with the verified letters marked.
* Indicate to the player whether or not the word is a palindrome. This recursive method receives just 1 String argument.

---

### Deliverables
* Submit all your files to a GitLab repository (`CS1120_Proj03_LastNamesOfTeamMembers`) including:
    * Program files
* Provide this information in every file in your project:
    ```python
    # Project No.:
    # Author:
    # Description:
    ```
**NOTE**: You may submit beyond the due date but your submission date/time will be recorded. The penalty for late submissions as stated in the course syllabus will be applied in grading any assignment submitted late.

---

### Design Requirements
You MUST use recursion for this project. Recall that recursion is when a method calls itself (one or more times), and each call might again call itself, over and over until some base condition is met and the methods return. This will be useful for finding a word on the board.

You should have a class called `BoggleBoard`, which includes the two-dimensional lists of letters, methods for filling and printing it, and a method that returns whether or not a given word is valid for the board. This last method should make use of another recursive method for verifying words.

You should have a separate `.py` file containing your `main()` function, which creates an instance of the board and runs the game (i.e. displays the board, asks player to find words, tells player if word is valid or not, etc.).

---

### Design Hints
* Generating a random character is a lot like generating a random integer. For example, you could use the following to generate a random character.
    ```python
    import string
    import random
    # Randomly choose a letter from all the ascii_uppercase
    someChar = random.choice(string.ascii_uppercase)
    print(someChar)
    ```
* You may want to use two coinciding 2-dimensional arrays to represent the boggle board - one that contains the letters, and one that keeps track of which cells have been visited already when verifying a word.
* For the recursion, think about how you might check the board if you were doing it by hand. You might start by scanning the array for the first letter of the word. If you find a match for the first letter, you would then check each of its neighbors for the next letter. If one of them matches, you check its neighbors, and so on, until either reaching the end of the word or finding no matches. Think about which part of this is the recursive step, and what the terminating condition(s) would be.
* You MUST use a recursive method with just 1 String argument to determine if the word is a palindrome.

---

### Additional Requirements
**Coding Standards**: You must adhere to all conventions applicable to writing programs. This includes the use of white spaces and indentations for readability, the use of comments to explain the meaning of various methods and attributes, and the conventions for naming classes, variables, method parameters and methods.

---

### Example Output 1
See a sample report below. Use the EXACT format/wording/spacing/labeling/... shown in sample. (use EXACT format - and NO HARDCODING of the data itself)

````

Enter seed: 9999
+---+ +---+ +---+ +---+
| L | | S | | Y | | U |
+---+ +---+ +---+ +---+
| P | | R | | A | | U |
+---+ +---+ +---+ +---+
| A | | K | | W | | V |
+---+ +---+ +---+ +---+
| L | | N | | A | | P |
+---+ +---+ +---+ +---+
Enter word (in UPPERcase): AWAY
Nice Job!
The word AWAY is not a palindrome.
+---+ +---+ +---+ +---+
| L | | S | |<Y>| | U |
+---+ +---+ +---+ +---+
| P | | R | |<A>| | U |
+---+ +---+ +---+ +---+
| A | | K | |<W>| | V |
+---+ +---+ +---+ +---+
| L | | N | |<A>| | P |
+---+ +---+ +---+ +---+

```

### Example Output 2
See a sample report below. Use the EXACT format/wording/spacing/labeling/... shown in sample. (use EXACT format - and NO HARDCODING of the data itself)

```

Enter seed: 9999
+---+ +---+ +---+ +---+
| L | | S | | Y | | U |
+---+ +---+ +---+ +---+
| P | | R | | A | | U |
+---+ +---+ +---+ +---+
| A | | K | | W | | V |
+---+ +---+ +---+ +---+
| L | | N | | A | | P |
+---+ +---+ +---+ +---+
Enter word (in UPPERcase): PLAY
I don't see that word.
The word PLAY is not a palindrome.
Are we looking at the same board?

```
```
