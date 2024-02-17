# Method 1. Reverse the word using slice
def word_reverse_slice(word):
    return word[::-1]

# Method 2. Using String function: reverse()
def word_reverse(word):
    return ''.join(reversed(word))


word = input("Enter a word: ")

#  convert it to lowercase for consistent comparison.
word = word.lower()

reversed_word = word_reverse_slice(word)
#reversed_word = word_reverse(word)

if word == reversed_word:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")
