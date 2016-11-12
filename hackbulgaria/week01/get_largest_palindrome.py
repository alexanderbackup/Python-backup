def get_largest_palindrome(n):

    for i in range(n-1, 0, -1):
        if str(i) == str(i)[::-1]:
            return i

print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))
print(get_largest_palindrome(671245176))
