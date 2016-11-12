import itertools

def goldbach(n):
    n_primes = []
    result = []
    for num in range(2,n):
        if all(num%i!=0 for i in range(2,num)):
            n_primes.append(num)
    #print(n_primes)
    for i in itertools.product(n_primes, repeat=2):
        if i[0] + i[1] == n and ((i[1], i[0]) not in result):
            result.append(i)
    return result

print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
#print(goldbach(1000))
