class TVShowProgress:

    def __init__(self, title, total_episodes):
        self.title = title
        self.total_episodes = total_episodes
        self.episodes_watched = 0

    def watch(self, eps_completed):
        if(eps_completed > self.total_episodes):
            print("Uh-oh!")
        self.episodes_watched += eps_completed
        return self.total_episodes
    
    def get_progress(self):
        percentage_completion = round((self.episodes_watched / self.total_episodes) * 100)
        return f"{percentage_completion}% complete of {self.title}"

# we're working at our Netflix competitor
# we have our TVShowProgress class and it's doing great

spongebob = TVShowProgress("Spongebob Squarepants", 10)
print(spongebob.get_progress())

spongebob.watch(2)
print(spongebob.get_progress())

spongebob.watch(2)
print(spongebob.get_progress())

# 10000 lines of code...

# you're not MEANT to do this
spongebob.episodes_watched = 1000

# I want you to call
spongebob.watch(1000) # this does the actual logic of tracking!

spongebob.episodes_watched = -4387
spongebob.title = None

print(spongebob.get_progress())
