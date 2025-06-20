def rolling_average(sample_size):
    recent_calls = []

    def _avg(num):
        recent_calls.append(num)
        if len(recent_calls) > sample_size:
            recent_calls.pop(0)
        return sum(recent_calls) / len(recent_calls)

    return _avg

get_rolling_average_3 = rolling_average(3)

print(get_rolling_average_3(1)) # 1 (average of 1)
print(get_rolling_average_3(2)) # 1.5 (average of 1,2)
print(get_rolling_average_3(3)) # 2 (average of 1,2,3)
print(get_rolling_average_3(2)) # 2.3333 (average of 2,3,2)
print(get_rolling_average_3(10)) # 2.3333 (average of 3,2,10)


# rolling average of 2 numbers

# 10,      20,      30,     20, 
#    ^15        ^25      ^25