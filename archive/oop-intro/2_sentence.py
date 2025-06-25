# Make a `Sentence` class which accepts some text as an input. The Sentence object should:
# - Validate whether the text is a sentence 
#   (starts with a capital letter and ends with '.', '?' or '!'.)
# - Have a `text` property (or **attribute**) which holds the original text.
# - Have an attribute which returns a dictionary containing important data about the sentence, 
#   such as the number of words, the number of characters and the number of non-alphabetical 
#   characters.
# - Allow the sentence to be recreated from new text, again validating it is correct.

# EXAMPLE USAGE

# SCREAMING_SNAKE_CASE_HAS_A_FUN_NAME - people use this for constants
# kebab-case-like-this - often used in URLs

# In Python we usually use snake_case_like_this - all lower case, with underscores between words
#   - we use snake_case_like_this for functions, variables

# why have I called this class "Sentence"?
# classes use PascalCaseLikeThis - no underscores between words, and capitals for Every Word
class Sentence:

    # ALL classes have an __init__ function
    # this is called when the class is initialised (created, made)
    def __init__(self, text):
        self.text = text

        self.is_valid = self._validate()

        self.data = self._generate_data()

    def _validate(self):
        if not self.text:
            return False
        # starts with a capital letter and ends with '.', '?' or '!'
        return self.text[0].isupper() and self.text[-1] in '.!?'
    
    def _generate_data(self):
        # words, characters, special characters
        words = len(self.text.split()) # number of words
        characters = len(self.text)
        special_characters = sum(1 for char in self.text if not char.isalpha() and not char.isspace())

        return {
            'words': words,
            'characters': characters,
            'special_characters': special_characters
        }
    
    def rebuild(self, new_text):
        self.text = new_text
        self.is_valid = self._validate()
        self.data = self._generate_data()


sen_1 = Sentence('This is not, really, a good sentence')

sen_2 = Sentence('This is a different sentence, but valid, I think?')

print(sen_1.text) # 'This is not, really, a good sentence'
# this is us storing DATA/STATE on an object
#print(sen_2.text) # 

print(sen_1.is_valid) # False - doesn't end with punctuation
#print(sen_2.is_valid) # True - meets all the rules

print(sen_1.data)
#print(sen_2.data)

sen_1.rebuild('This is a better sentence!')

print(sen_1.text) # This is a better sentence!'

print(sen_1.data) # {'words': 5, 'characters': 26, 'special': 5}



# when I create a new INSTANCE of a class it VERY often requires some data, e.g.:
# dave = Customer('dave', 'dave@dave.com', 198278917) # self = dave
# liam = Customer('liam') # self = liam
# sam = Customer('sam') # self = same
