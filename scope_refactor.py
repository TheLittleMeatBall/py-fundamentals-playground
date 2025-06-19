# let's "refactor" 
# refactor -> polish it... more specifically "polishing the code WITHOUT CHANGING HOW IT FUNCTIONS"
# Problem 1: we're messing with global scope variables - "global state"
# Problem 2: the function is doing more than one thing

def add_bonus(scores, bonus):
    return [score + bonus for score in scores]

def calculate_average(scores):
    return sum(scores) / len(scores)

def do_something(func):
    # do a bunch of processing to calculate a result
    result = {}
    func() # this is IDENTICAL to calling whatever_function_was_passed_in()
    pass

do_something(calculate_average)
do_something(add_bonus)

# def add_bonus_and_average():
    # # we don't really want to be using these keyword in PRODUCTION code
    # global scores

    # for i in range(len(scores)):
    #     scores[i] += 5

    # global average_score
    # average_score = sum(scores) / len(scores)

scores = [ 10, 20, 30, 40]
updated_scores = add_bonus(scores, 5)
average_score = calculate_average(updated_scores)

# add_bonus_and_average()
print("Original scores: ", scores)
print("Updated scores: ", updated_scores)
print("Average score:", average_score)