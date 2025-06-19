# We want a separate file for our tests
from longest_word import get_longest_word

#get_longest_word('She built a house of stone!')
# --> built
# "it correctly ignores punctuation"
# "it gets the first word when there are multiple matches"

#get_longest_word('')
# --> ''
# "when given an empty string, it returns an empty string"

#get_longest_word(1278678)
# --> ''
# "when given a non-string, it returns an empty string"

# pytests looks for:
#  - files named test_XXXX.py
#  - functions named test_XXXX()

def test_gets_longest_word():
    assert get_longest_word('green is my favourite colour') == 'favourite'

def test_gets_longest_word_when_multiple_matches():
    assert get_longest_word('She built a house of stone') == 'built'


def test_gets_longest_word_when_multiple_matches_and_removes_punctuation():
    assert get_longest_word('She built a house of stone!') == 'built'


# later, I'll add another test for punctuation