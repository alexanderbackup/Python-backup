#Counting substrings
def count_substrings(haystack, needle):
	return len([i for i in haystack.replace(' ', '').replace(needle, ' ') if i ==' '])


#Sum Numbers in Matrix
def sum_matrix(m):
    return sum(sum(i) for i in m)


# NaN Expand
def nan_expand(times):
    if times == 0:
        return ""
    else:
        return ' '.join(["Not a" for i in range(times)])+" NaN"


# Integer prime factorization
def prime_factorization(n):
	result = []
	temp = ()
	pi = 2
	ai = 0
	while pi*pi <= n:
		while (n % pi) == 0:
			ai += 1
			temp = (pi, ai)
			n //= pi
		if temp not in result and temp != (): result.append(temp)
		pi += 1
		ai = 0
	if n > 1:
		ai += 1
		temp = (n, ai)
		result.append(temp)
	return result

def group(smth):
    result = []
    temp = []
    for i in smth:
        if temp == []:
            temp.append(i)
        elif i == temp[-1]:
            temp.append(i)
        else:
            result.append(temp)
            temp = [i]
    result.append(temp)
    return result


# Longest subsequence of equal consecutive elements
def max_consecutive(items):
    result = []
    temp = []
    for i in items:
        if temp == []:
            temp.append(i)
        elif i == temp[-1]:
            temp.append(i)
        else:
            result.append(temp)
            temp = [i]
    result.append(temp)
    return len(max(result, key=lambda x: len(x)))

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
## Word Count
#def word_count():
#	pass


