# We want to:

# 1. Prevent direct tampering with internal data - the state of the class
# 2. Validate changes before they're made - people (other devs) should interact with our class
# 3. Keep each instance in a consistent, valid state

# "Private" Attributes - using the double underscore
class TVShowProgress:

    def __init__(self, title, total_episodes):
        self.__title = title
        self.__total_episodes = total_episodes
        self.__episodes_watched = 0 

    def watch(self, eps_completed):
        if(eps_completed > self.__total_episodes):
            print("Uh-oh!")
            return
        self.__episodes_watched += eps_completed # inside the class this works as normal!
        return self.__total_episodes
    
    def get_progress(self):
        percentage_completion = round((self.__episodes_watched / self.__total_episodes) * 100)
        return f"{percentage_completion}% complete of {self.__title}"


spongebob = TVShowProgress("Spongebob Squarepants", 10)
print(spongebob.get_progress())

spongebob.watch(2)
print(spongebob.get_progress())


# the single underscores acts as a CONVENTION saying "please don't change this variable manually from outside the class"

# the double underscore...
# spongebob.__episodes_watched = -453986892

# {'title': 'Spongebob Squarepants', 'total_episodes': 10, '_TVShowProgress__episodes_watched': 2}
# double underscore triggers "NAME MANGLING"
# python internally changes the name from __episodes_watched to _TVShowProgress__episodes_watched
print(spongebob.__dict__)


print(spongebob.get_progress())

spongebob.__title = None
spongebob.__episodes_watched = -543987

print(spongebob.get_progress())