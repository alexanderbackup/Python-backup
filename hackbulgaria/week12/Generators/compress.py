
def compress(iterable, mask):
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]
    
    

