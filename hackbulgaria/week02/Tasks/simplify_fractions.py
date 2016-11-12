def simplify_fraction(fraction):
    check = min(fraction)
    while max(fraction) % check != 0 or min(fraction) % check != 0:
        check -= 1
    return tuple(int(i/check) for i in fraction)



#print(simplify_fraction((1, 9)))
#print(simplify_fraction((1, 7)))
#print(simplify_fraction((4, 10)))
#print(simplify_fraction((63,462)))
