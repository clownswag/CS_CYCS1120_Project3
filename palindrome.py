class IsPalindrome:
    def __init__(self, word):
        self.word = word
    
    def is_palindrome(self):
        def isPalindromeUtil(str1, left, right):
            if left >= right:
                return True
            if str1[left] != str1[right]:
                return False
            return isPalindromeUtil(str1, left+1, right-1)
        left = 0
        right = len(self.word) - 1
        result = isPalindromeUtil(self.word, left, right)
        if result == True:
            print(f'The word {self.word.upper()} is a palindrome.')
        else:
            print(f'The word {self.word.upper()} is not a palindrome.')
            return False
    
# checker = IsPalindrome("tacocat")
# checker.is_palindrome()

# The word PLAY is not a palindrome.