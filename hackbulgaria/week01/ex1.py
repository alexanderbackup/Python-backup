# A function for counting the digits of a number
def sum_of_digits(number):
    return sum(int(i) for i in str(abs(number)))


# Create list with the digits of a number
def to_digits(number):
    return [int(i) for i in str(abs(number))]


# Create number from array
def to_number(digits):
    return int(''.join(map(str, digits)))


# Count the vowels in a string
def count_vowels(string):
    return len([i for i in string.lower() if i in 'aoeiuy'])


# Count the consonants in a string
def count_consonants(string):
    return len([i for i in string.lower() if i in "bcdfghjklmnpqrstvwxz"])


# Check if a given number is prime
def prime_number(number):
    return all(number % i for i in range(2, number))


# Sum of the factorials of the digits in the number
def fact_digits(n):
    result = []
    for i in [int(i) for i in str(n)]:
        j = 1
        for n in range(1, i+1):
            j *= n
        result.append(j)
    return sum(result)


# fibonacci sequince
def fibonacci(number):
    a,b = 1,1
    result = []
    for i in range(number):
        result.append(a)
        a,b = b,a+b
    return result

#fibonacci number
def fib_number(n):
    a,b = 1,1
    result = []
    for i in range(n):
        result.append(a)
        a,b = b,a+b
    return int(''.join(map(str, result)))

# Check if a given string is palindrome
def palindrome(n):
    return True if str(n) == str(n)[::-1] else False

# Dictionary with all characters from a string
def char_histogram(string):
    result = {}
    for i in string:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return result

