
def cycle(iterable):
    counter = 0
    smth = [i for i in iterable]
    while True:
        if counter == len(iterable):
            counter = 0
        yield smth[counter]
        counter += 1
