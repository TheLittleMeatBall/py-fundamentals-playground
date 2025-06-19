# Create a function called `get_longest_word` that takes a string representing a sentence of space-separated words and returns the longest word in a sentence

# If there are multiple longest words, it should return to the one that appears first in the sentence

# Ignore punctuation

# what does a test look like?

# Description: what behaviour of the function do we want to test?
# Assertion: showing dominance over the function
#             **saying something is how it is**

# BUT what does it look like in code

# Neils Rubbish Testing Framework:
#print('it correctly gets the longest word')
#print(get_longest_word('green is my favourite colour'))

# pytest

# we want to install pytest

def get_longest_word(sentence):
    words = sentence.split()
    longest_word = ''

    for word in words:
        for char in word:
            # remove any that aren't alphabet
        if(len(word) > len(longest_word)):
            longest_word = word
    
    return longest_word