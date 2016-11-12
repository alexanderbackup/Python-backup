# generate_numbers.py
import sys
from random import randint


def main():
    sys.argv[0] = 'generate_numbers.py'
    filename = sys.argv[1]
    n = sys.argv[2]
    f = open(filename, 'w')
    for i in range(int(n)):
        f.write(str(randint(1, 1000))+' ')
            
if __name__ == '__main__':
    main()
