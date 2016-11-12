def increasing_or_decreasing(seq):
    if seq[0] != seq[-1]:
        if sorted(seq) == seq:
            return 'Up!'
        elif sorted(seq, reverse=True) == seq:
            return 'Down!'

    return False

print(increasing_or_decreasing([1,2,3,4,5]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([9,8,7,6]))
