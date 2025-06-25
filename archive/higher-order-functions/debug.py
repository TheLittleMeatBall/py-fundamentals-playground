# breakpoint
print("Starting program")

def is_palindrome(s):

    return s == s[::-1]

def factorial(n):
    print("Calculating factorial,", n)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def main():
    words = ["racecar", "hello", "level", "world"]
    for word in words:
        print(f"Is '{word}' a palindrome? → {is_palindrome(word)}")

    print("\nFactorials:")
    for i in range(1, 6):
        print(f"{i}! = {factorial(i)}")

    print("\nFizzBuzz from 1 to 15:")
    for i in range(1, 16):
        print(fizzbuzz(i))


main()