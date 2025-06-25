from datetime import datetime, date
# time and date is PAINFUL for developers - NEVER write your own date/time handling code
# general advice: ALWAYS use UTC time for everything
# UTC = Universal Time Coordinated (it's French)
# UTC is the ACTUAL TIME IN THE UNIVERSE at which things happen
# (you can then DISPLAY it in local time if you want)
# but you do not RESPECT the concept of local time

# We want to:

# 1. Prevent direct tampering with internal data - the state of the class
# 2. Validate changes before they're made - people (other devs) should interact with our class
# 3. Keep each instance in a consistent, valid state

from copy import deepcopy

# "Private" Attributes - using the double underscore
class TVShowProgress:

    def __init__(self, title, total_episodes):
        self.__title = title
        self.__total_episodes = total_episodes
        self.__episodes_watched = [] 

    def watch(self, eps_completed):
        if(eps_completed > self.__total_episodes):
            print("Uh-oh!")
            return
        current_time = datetime.now().date()

        self.__episodes_watched.append({
            "timestamp": current_time,
            "watched": eps_completed
        })
      
        total_eps_watched = sum(ep["watched"] for ep in self.__episodes_watched)
        return self.__total_episodes - total_eps_watched
    
    def get_progress(self):
        total_eps_watched = sum(ep["watched"] for ep in self.__episodes_watched)
        percentage_completion = round((total_eps_watched / self.__total_episodes) * 100)
        return f"{percentage_completion}% complete of {self.__title}"
    
    @property
    # getter
    # the @property decorator allows us to access methods in a class but without calling them like functions
    # so later, I can say "spongebob.episodes_watched"
    def episodes_watched(self):
        # transform the data
        # validate the data before returning it
        # return a copy instead of the original
        return deepcopy(self.__episodes_watched)

    @episodes_watched.setter
    def episodes_watched(self, new_eps_watched):
        # now I have the power to do what I want when people set data to this property
        if not isinstance(new_eps_watched, list):
            raise ValueError("how dare you! lists only!")
        
        # check that the total episodes watched isn't bigger than the total episodes
        
        # I could transform the data
        self.__episodes_watched.append(new_eps_watched)
        return self.__episodes_watched


spongebob = TVShowProgress("Spongebob Squarepants", 10)


# this doesn't work YET but I'd love to be able to add new data like this
spongebob.episodes_watched = [ { "timestamp": date(2024,6,3), "watched": 5}]



print(spongebob.get_progress())

spongebob.watch(2)
print(spongebob.get_progress())


spongebob.watch(6)

print(spongebob.episodes_watched)

uhoh = spongebob.episodes_watched

uhoh.append("hahahha")

print(spongebob.episodes_watched)

