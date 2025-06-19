import pprint

# assigning something into this scope
pp = pprint.PrettyPrinter(indent = 4)

# again!
default_knowledge = 'Massive'

# this isn't intended to be "good" code, it's intended to play around with scope
def create_personal_statement(knowledge):
    name = 'Bernadine'
    
    def intro_spect(b):
        # I ONLY declare game in this function, nothing else
        game = 'Data'
        return f'"{b} is the name. "{game}" is the game. My knowledge level is "{knowledge}.'
    
    return intro_spect(name)

print(create_personal_statement(default_knowledge))

# WHAT LIVES IN GLOBAL SCOPE?
# 1. pp
# 2. default_knowledge
# 3. create_personal_statement

# WHAT LIVES IN local scope for create_personal_statement?
# 1. name
# 2. intro_spect