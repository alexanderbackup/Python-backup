from os import listdir
from os.path import isfile, join

def test():
    mypath = './Book'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for _file in onlyfiles:
        new_file = mypath + '/' + _file
        with open(new_file, encoding='ascii') as f:
            for i in f:
                if i[0] == '#':
                    while True:
                        ans = input()
                        if ans == ' ':
                            break
                        else:
                            print('Press space!') 
                yield i
                    
for i in test():
    print(i)
